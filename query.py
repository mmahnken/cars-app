"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *
init_app()

# Part 2: Write queries

# Get the brand with the **id** of 8.
q1 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
q2 = Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
q8 = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following function.
def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter_by(year=year).all()
    out = ""
    for m in models:
        if m.brand:
            out = out + "%s | %s | %s\n" % (m.name, m.brand.name, m.brand.headquarters)
    print out


# Fill in the following function.
def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    all_brands = Brand.query.all()

    out = ""
    for b in all_brands:
        out = out + b.name + "\n"
        for m in b.models:
            out = out + "\t%s\n" % m.name
    print out

# Part 2.5: Discussion Questions

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(brand_name='Ford')``?

# This is just a query object, not a result. So you get a
# flask_sqlalchemy.BaseQuery object. If you were to add .one() to the end
# of the query, you'd get a Brand object.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# An association table acts as the middleman in a many-to-many
# relationship.
# For example, if you want tables A and B to have an M2M relationship, you'd
# create a table AB which just had AB pairings in it.
# Then each of A and B would have a one-to-many
# relationship to the AB table. If, however, there were actual *information*
# associated with the pairing (so the AB table would have more than just id, A,
# and B fields), then the table that manages the relationship between
# A and B would be a "middle" table, not an association table.

# Part 3
def search_brands_by_name(mystr):
    results = Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()
    return results


def get_models_between(start_year, end_year):
    results = Model.query.filter(Model.year > start_year, Model.year < end_year).all()
    return results

