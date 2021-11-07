<template>
  <v-container>
    <Card
        @like="like"
        @bad="bad"
        :title="this.showData.title"
        :description="this.showData.description"
        :image="this.showData.image"
        :creator="this.showData.creator"
        :creator-img="this.showData.creatorImg"
    />
  </v-container>
</template>

<script>
import Card from "@/components/Card";
import {collection} from "firebase/firestore";
import {getFirestore, query, orderBy, getDocs, getDoc, doc, updateDoc} from "firebase/firestore"
import {getAuth} from "firebase/auth";
import firebase from "firebase/compat";

export default {
  name: 'Home',
  components: {
    Card
  },
  data() {
    return {
      data: [],
      showData: {},
      index: 0,
      creatorImg: getAuth().currentUser.photoURL,
    }
  },
  async mounted() {
    const db = getFirestore();
    const userRef = collection(db, 'works')
    const q = query(userRef, orderBy(firebase.firestore.FieldPath.documentId()));
    const querySnapshot = await getDocs(q)
    querySnapshot.forEach((doc) => {
      this.data.push({
        title: doc.data().title,
        explation: doc.data().explation,
        thumnail: doc.data().thumnail,
        creator: doc.data().creator,
        creatorImg: doc.data().creatorImg,
        docId: doc.id
      })
    });
    this.showData = {
      title: this.data[this.index].title,
      description: this.data[this.index].explation,
      image: this.data[this.index].thumnail,
      creator: this.data[this.index].creator,
      creatorImg: this.creatorImg,
      docId: this.data[this.index].docId
    }
  },
  methods: {
    async updateCounter(pm) {
      console.log(pm)
      const db = getFirestore();
      const docRef = doc(db, 'works', this.showData.docId)
      const docSnap = await getDoc(docRef)
      if (pm) {
        await updateDoc(docRef, {
          LIKE_NUM: docSnap.data().LIKE_NUM + 1
        })
      } else {
        await updateDoc(docRef, {
          BAD_NUM: docSnap.data().BAD_NUM + 1
        })
      }
    },
    async like() {
      await this.updateCounter(true);
      this.renderNext()
    },
    async bad() {
      await this.updateCounter(false);
      this.renderNext()
    },
    renderNext() {
      this.index++;
      if(this.index>this.data.length-1) {
        this.index = 0;
      }
      this.showData = {
        title: this.data[this.index].title,
        description: this.data[this.index].explation,
        image: this.data[this.index].thumnail,
        creator: this.data[this.index].creator,
        creatorImg: this.creatorImg,
        docId: this.data[this.index].docId
      }
    }
  }
}
</script>
