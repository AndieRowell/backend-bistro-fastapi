-- categories
INSERT INTO category (name)
VALUES ('Drinks')

INSERT INTO category (name)
VALUES ('Appetizer')

INSERT INTO category (name)
VALUES ('Breakfast')

INSERT INTO category (name)
VALUES ('Lunch')

INSERT INTO category (name)
VALUES ('Dinner')

INSERT INTO category (name)
VALUES ('Dessert')

-- cuisines

INSERT INTO cuisine (name)
VALUES ('Thai')

INSERT INTO cuisine (name)
VALUES ('Vietnamese')

INSERT INTO cuisine (name)
VALUES ('American')

INSERT INTO cuisine (name)
VALUES ('Japanese')

INSERT INTO cuisine (name)
VALUES ('Korean')

INSERT INTO cuisine (name)
VALUES ('French')

INSERT INTO menu_item (
    -- id,
    title,
    -- cuisine_id,
    cuisine_id,
    -- category_id,
    category_id,
    description,
    price,
    spicy_level
  )
VALUES (
    -- id:integer,
    'tom yum soup',
    -- cuisine_id:integer,
    cuisine_id:integer,
    -- category_id:integer,
    category_id:integer,
    'a deliscious sour and spicy soup',
    '9.99',
    spicy_level:integer
  );
