PGDMP     #                      z           ProyectoFinal    14.5    14.5     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16394    ProyectoFinal    DATABASE     k   CREATE DATABASE "ProyectoFinal" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "ProyectoFinal";
                postgres    false            �            1259    16488 	   productos    TABLE     �   CREATE TABLE public.productos (
    codigo_de_barras character varying(6) NOT NULL,
    nombre character varying(40) NOT NULL,
    marca character varying(40) NOT NULL,
    precio integer NOT NULL,
    cantidad_en_almacen integer NOT NULL
);
    DROP TABLE public.productos;
       public         heap    postgres    false            �          0    16488 	   productos 
   TABLE DATA           a   COPY public.productos (codigo_de_barras, nombre, marca, precio, cantidad_en_almacen) FROM stdin;
    public          postgres    false    209   	       \           2606    16492    productos productos_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_pkey PRIMARY KEY (codigo_de_barras);
 B   ALTER TABLE ONLY public.productos DROP CONSTRAINT productos_pkey;
       public            postgres    false    209            �   �   x�U�An�0E���T�1�,#4�Jj�u�$����G��:V�����͸ٗO:��O��cXtb E��,��ͿO\�����B��.�:#���zgo�)*F�����5l1FZ���&7�c��X��{�e�C�;�U�@[!�D�ǺQ�ޯ��J���@e�(���y���e3UZ���U���1Lte�lԮU��׵��� *��w��ҝ#��ޟ��U�<!~ �Uj"     