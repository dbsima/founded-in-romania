--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: company; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE company (
    id integer NOT NULL,
    name character varying(80),
    description text,
    twitter character varying(64),
    founded_year integer,
    founders character varying(180),
    url text,
    bitly_url character varying(180),
    logo_submited text,
    logo character varying(180),
    contact_email character varying(120),
    contact_name character varying(120),
    date_submit timestamp without time zone,
    status character varying(64)
);


ALTER TABLE public.company OWNER TO ubuntu;

--
-- Name: company_id_seq; Type: SEQUENCE; Schema: public; Owner: ubuntu
--

CREATE SEQUENCE company_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_id_seq OWNER TO ubuntu;

--
-- Name: company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubuntu
--

ALTER SEQUENCE company_id_seq OWNED BY company.id;


--
-- Name: pair; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE pair (
    id integer NOT NULL,
    key character varying(80),
    val integer
);


ALTER TABLE public.pair OWNER TO ubuntu;

--
-- Name: pair_id_seq; Type: SEQUENCE; Schema: public; Owner: ubuntu
--

CREATE SEQUENCE pair_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pair_id_seq OWNER TO ubuntu;

--
-- Name: pair_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubuntu
--

ALTER SEQUENCE pair_id_seq OWNED BY pair.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE "user" (
    id integer NOT NULL,
    login character varying(80),
    password character varying(128)
);


ALTER TABLE public."user" OWNER TO ubuntu;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: ubuntu
--

CREATE SEQUENCE user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO ubuntu;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubuntu
--

ALTER SEQUENCE user_id_seq OWNED BY "user".id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ubuntu
--

ALTER TABLE ONLY company ALTER COLUMN id SET DEFAULT nextval('company_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ubuntu
--

ALTER TABLE ONLY pair ALTER COLUMN id SET DEFAULT nextval('pair_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ubuntu
--

ALTER TABLE ONLY "user" ALTER COLUMN id SET DEFAULT nextval('user_id_seq'::regclass);


--
-- Data for Name: company; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY company (id, name, description, twitter, founded_year, founders, url, bitly_url, logo_submited, logo, contact_email, contact_name, date_submit, status) FROM stdin;
9	Campadillo		@campadillo	2014	\N	http://campadillo.com	\N	http://campadillo.com/img/campadillo_logo_white.png	90ac3d6b-a1ba-4eca-8dca-f879037dfd8e.png	office@campadillo.com	Cosmin Stamate	2014-10-23 22:59:31	accepted
10	7Out		@7OutApp	1999	\N	http://get7out.com	\N	http://get7out.com/press-kit.zip	8c35f491-4020-453c-b01f-eb45d589888c.png	support@7out.us	support	2014-10-25 15:36:00	accepted
1	FaceRig		@FaceRig	2013	\N	http://www.facerig.com	\N	http://facerig.com/images/downloads/AvatarScreenshots_8.zip	54534b25-de9a-4c22-80f8-dfb91ef8341b.png	dont@know.yet	Don't know	2014-10-14 13:28:14	pending
12	Eventya		@eventyaeu	1991	\N	http://eventya.eu/	\N	http://cldup.com/FsMoB3eCe2.png	83bff4e8-da74-4b7f-9e57-01d56c672fb6.png	imunteanu@i-consult.ro	Ionuț Munteanu	2014-10-28 23:15:06	accepted
11	GloriaFood		@gloriafood	2013	\N	http://www.gloriafood.com	\N	https://www.gloriafood.com/media-kit	f89601e0-962d-4552-8840-2d57f9899afd.png	oliver.auerbach@gloriafood.com	Oliver Auerbach	2014-10-28 15:17:05	accepted
4	CyberGhost		@cyberghost_EN	2011	\N	http://www.cyberghostvpn.com	\N	http://www.cyberghostvpn.com/download/press/cg5_press_kit_en.rar	809ad3ad-8366-40b6-b565-7d8de001d788.png	press.office@cyberghost.ro	Press	2014-10-14 13:39:10	accepted
2	Two Tap		@twotapbuy	2013	\N	http://twotap.com	\N	http://twotap.com/public/twotap-mediakit.zip	28398549-8f2c-4ccb-afbc-77e27a904545.png	press@twotap.com	Press	2014-10-14 13:25:37	accepted
6	Juqster		@Juqster	2014	\N	http://www.juqster.com	\N	http://www.juqster.com/imgs/JuqsterLogo1200x1200WhiteBackground.png	f8b0f165-0a6f-4fab-a62b-e460ef2488ed.png	radu@juqster.com	Tapus Radu	2014-10-16 13:45:57	accepted
3	Tintag		@Tintagapp	1999	\N	http://thetintag.com/	\N	http://thetintag.com/TintagPressKit.zip	258288b8-d165-44cc-b3d0-599da09c05b4.png	office@tint.ag	Office	2014-10-14 13:35:11	accepted
8	Moqups		@moqups	2012	\N	https://moqups.com	\N	https://github.com/Evercoder/mediakit	2285ca13-2277-45ef-bfc8-41fe662ffa80.png	emil@moqups.com	Emil Tamaș	2014-10-22 13:43:14	accepted
\.


--
-- Name: company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ubuntu
--

SELECT pg_catalog.setval('company_id_seq', 12, true);


--
-- Data for Name: pair; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY pair (id, key, val) FROM stdin;
1	since	1414545306
\.


--
-- Name: pair_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ubuntu
--

SELECT pg_catalog.setval('pair_id_seq', 1, true);


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY "user" (id, login, password) FROM stdin;
1	admin	pbkdf2:sha1:1000$aotiKVlo$638179d446a4a9fbdb562ba34aba14c7efac8434
\.


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ubuntu
--

SELECT pg_catalog.setval('user_id_seq', 1, true);


--
-- Name: company_pkey; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY company
    ADD CONSTRAINT company_pkey PRIMARY KEY (id);


--
-- Name: pair_key_key; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY pair
    ADD CONSTRAINT pair_key_key UNIQUE (key);


--
-- Name: pair_pkey; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY pair
    ADD CONSTRAINT pair_pkey PRIMARY KEY (id);


--
-- Name: user_login_key; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_login_key UNIQUE (login);


--
-- Name: user_pkey; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

