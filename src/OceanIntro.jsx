import React,{useEffect,useRef,useState} from 'react';
import gsap from 'gsap';
import {ArrowDown,Pause,Play} from '@phosphor-icons/react';
import './ocean-intro.css';

export default function OceanIntro(){
 const root=useRef(null),film=useRef(null),manual=useRef(false);
 const [paused,setPaused]=useState(false),[ended,setEnded]=useState(false);
 const [reduced,setReduced]=useState(()=>matchMedia('(prefers-reduced-motion: reduce)').matches);
 const [ready,setReady]=useState(false);
 const enter=()=>{manual.current=true;film.current?.pause();document.querySelector('.site-header')?.scrollIntoView({behavior:reduced?'instant':'smooth',block:'start'});};
 useEffect(()=>{const mq=matchMedia('(prefers-reduced-motion: reduce)');const change=()=>setReduced(mq.matches);mq.addEventListener('change',change);return()=>mq.removeEventListener('change',change)},[]);
 useEffect(()=>{
  let active=true;
  Promise.all(['/assets/intro-ocean.webp','/assets/intro-ship-waterline.webp'].map(src=>new Promise(resolve=>{let im=new Image();im.onload=resolve;im.onerror=resolve;im.src=src}))).then(()=>active&&setReady(true));
  return()=>{active=false};
 },[]);
 useEffect(()=>{
  if(!ready||reduced)return;
  const ctx=gsap.context(()=>{
   film.current=gsap.timeline({onComplete:()=>{setEnded(true);if(!manual.current&&root.current.getBoundingClientRect().top>-80&&!document.hidden)enter()}})
    .fromTo('.intro-progress span',{scaleX:0},{scaleX:1,duration:6,ease:'none'},0)
    .fromTo('.intro-title > span',{opacity:0,y:22},{opacity:1,y:0,duration:1.5,stagger:.22,ease:'power2.out'},.35);
  },root);
  const cancelAuto=()=>{manual.current=true};
  const key=e=>{if(['ArrowDown','ArrowUp','PageDown','PageUp','Home','End',' '].includes(e.key))cancelAuto()};
  const visibility=()=>{if(document.hidden){film.current?.pause();setPaused(true)}};
  window.addEventListener('wheel',cancelAuto,{passive:true});window.addEventListener('touchstart',cancelAuto,{passive:true});window.addEventListener('keydown',key);document.addEventListener('visibilitychange',visibility);
  return()=>{ctx.revert();window.removeEventListener('wheel',cancelAuto);window.removeEventListener('touchstart',cancelAuto);window.removeEventListener('keydown',key);document.removeEventListener('visibilitychange',visibility)};
 },[ready,reduced]);
 useEffect(()=>{
  document.body.classList.add('has-ocean-intro');
  const onScroll=()=>{const box=root.current?.getBoundingClientRect();document.body.classList.toggle('intro-nav-ready',!!box&&box.bottom<innerHeight*.65)};
  onScroll();window.addEventListener('scroll',onScroll,{passive:true});
  return()=>{document.body.classList.remove('has-ocean-intro','intro-nav-ready');window.removeEventListener('scroll',onScroll)};
 },[]);
 const toggle=()=>{if(ended){manual.current=true;setEnded(false);film.current?.restart();setPaused(false)}else{film.current?.paused(!paused);setPaused(!paused)}};
 return <section ref={root} className={'ocean-intro '+(paused||reduced||!ready?'intro-paused':'')} aria-label="PortTriage cinematic introduction">
  <div className="intro-world" aria-hidden="true"><div className="intro-sea"/><div className="intro-water-light"/><div className="intro-wave-surface"/><div className="intro-vessel"><img src="/assets/intro-ship-waterline.webp" alt=""/></div></div>
  <div className="intro-shade"/>
  <div className="intro-content"><img className="intro-brand" src="/brand/porttriage-logo-reverse.svg" alt="PortTriage"/><p className="intro-kicker">A clearer course for import operations</p><h1 className="intro-title"><span>Import operations,</span><span>clarified.</span></h1><p className="intro-description">Sourced milestones. Accountable handoffs.</p></div>
  <div className="intro-bottom"><span>Concept preview · Synthetic data</span><div>{!reduced&&<button onClick={toggle} aria-label={ended?'Replay intro':paused?'Play intro':'Pause intro'}>{paused?<Play size={17}/>:<Pause size={17}/>}<span>{ended?'Replay':paused?'Play':'Pause'}</span></button>}<button onClick={enter}>{reduced?'Continue to website':'Skip intro'}<ArrowDown size={18}/></button></div></div>
  {!reduced&&<div className="intro-progress" aria-hidden="true"><span/></div>}
 </section>
}
