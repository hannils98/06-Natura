create table places (
    id SERIAL,
    name text,
    description text,
    source text,
    latitude double PRECISION,
    longitude double PRECISION,

    primary key(id)
);

create table is_in (
    place_id int,
    sub_place_id int,

    primary key(place_id, sub_place_id),
    foreign key (sub_place_id) references places(id),
    foreign key (place_id) references places(id)

);

create table categories (
    name text,
    id serial,

    primary key(id)
);

create table place_has_cat (
    cat_id int,
    place_id int,

    primary key(cat_id, place_id),
    foreign key (cat_id) references categories(id),
    foreign key (place_id) references places(id)

);

create table ratings (
    userid int,
    placeid int,
    rating int,
    datetime timestamptz,

    primary key(userid, placeid),
    foreign key (userid) references "user"(id),
    foreign key (placeid) references places(id)
);

create table user_images (
    userid int,
    placeid int,
    pic text,
    alt text,
    datetime timestamptz,
    
    primary key(pic),
    foreign key (userid) references "user"(id),
    foreign key (placeid) references places(id)

);

create table admin_images (
    placeid int,
    pic text,
    alt text,
    description text,
    datetime timestamptz,
    
    primary key(pic),
    foreign key (placeid) references places(id)
);



