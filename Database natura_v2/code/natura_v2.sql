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



