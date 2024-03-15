# WildHook Testing Guide:

## Overview 
The testign ahs been split between automated and manual. All sections have been put through rigorous manual testing. Automated testing was carried out on two models details as below. The tests.py files are available in the directory of each App.

## Automated Testing Guide
1. [Introduction](#introduction)
2. [Products App Testing](#product-model-testing)
    - [Category Model Testing](#category-model-testing)
        - [Test Case: Category Model String Representation](#test-case-category-model-string-representation)
        - [Test Case: Category Model Friendly Name](#test-case-category-model-friendly-name)
    - [Product Model Testing](#product-model-testing)
        - [Test Case: Product Model String Representation](#test-case-product-model-string-representation)
        - [Test Case: Product Model Default Has Sizes](#test-case-product-model-default-has-sizes)
        - [Test Case: Product Model Offer Price Nullable and Blank](#test-case-product-model-offer-price-nullable-and-blank)
        - [Test Case: Product Model Label Choices](#test-case-product-model-label-choices)
3. [Conclusion](#conclusion) 
4. [Automated testing for Blog App](#automated-testing-for-blog-app)
    - [Introduction](#introduction)
    - [Post Model Testing](#post-model-testing)
    - [Test Case: Post Model Title](#test-case-post-model-title)
    - [Test Case: Post Model Slug](#test-case-post-model-slug)
    - [Test Case: Post Model Absolute URL](#test-case-post-model-absolute-url)
    - [Conclusion](#conclusion)
## Manual Testing Guide
4. [Blog App](#blog-app)
   - [Blog App Models](#blog-app-models)
   - [Blog App Views](#blog-app-views)
5. [Checkout App](#checkout-app)
   - [Checkout Models](#checkout-models)
   - [Checkout Views](#checkout-views)
6. [Products App](#products-app)
   - [Products Models](#products-models)
   - [Products Views](#products-views)
7. [Profiles App](#profiles-app)
   - [Profile Models](#profile-models)
   - [Profile Views](#profile-views)
8. [Reviews App](#reviews-app)
   - [Review Models](#review-models)
   - [Review Views](#review-views)
9. [User Interaction Testing](#user-interaction-testing)

# Automated Testing Guide

## Automated testing for Product and Category Models
## Introduction
This document outlines the automated testing procedures and results for the models `Product` and `Category` in the Django application. The tests were conducted to ensure the correctness and reliability of these models.


## Products App Testing
### Category Model Testing

#### Test Case: Category Model String Representation
- **Objective**: Verify that the string representation of the `Category` model returns the correct name.
- **Setup**: Create a `Category` instance with a specific name.
- **Expected Result**: The string representation of the `Category` model should return the assigned name.
- **Result**: Test passed successfully.

#### Test Case: Category Model Friendly Name
- **Objective**: Ensure that the method `get_friendly_name` returns the correct friendly name.
- **Setup**: Create a `Category` instance with a specific friendly name.
- **Expected Result**: The method `get_friendly_name` should return the assigned friendly name.
- **Result**: Test passed successfully.

### Product Model Testing

#### Test Case: Product Model String Representation
- **Objective**: Verify that the string representation of the `Product` model returns the correct name.
- **Setup**: Create a `Product` instance with a specific name.
- **Expected Result**: The string representation of the `Product` model should return the assigned name.
- **Result**: Test passed successfully.

#### Test Case: Product Model Default Has Sizes
- **Objective**: Ensure that the `has_sizes` field defaults to `False`.
- **Setup**: Create a `Product` instance without specifying the `has_sizes` field.
- **Expected Result**: The `has_sizes` field should be `False` by default.
- **Result**: Test passed successfully.

#### Test Case: Product Model Offer Price Nullable and Blank
- **Objective**: Verify that the `offer_price` field is nullable and blank.
- **Setup**: Create a `Product` instance without specifying the `offer_price` field.
- **Expected Result**: The `offer_price` field should be nullable and blank.
- **Result**: Test passed successfully.

#### Test Case: Product Model Label Choices
- **Objective**: Ensure that the `label` field contains the correct choices.
- **Setup**: Get the choices for the `label` field.
- **Expected Result**: The `label` field should contain the choices specified in the `LABEL_CHOICES` constant.
- **Result**: Test pass

# Automated testing for Blog App
# Automated Testing Documentation for WildHook Blog App

## Introduction 

This document outlines the automated testing conducted for the WildHook Blog App. The purpose of these tests is to ensure the correctness and functionality of the blog's Post model.

## Post Model Testing 

In this section, we conduct automated tests for the Post model to ensure its attributes and methods function as expected.

### Test Case: Post Model Title 

**Objective:**  
Ensure that the title of the Post model is correctly set.

**Test Steps:**  
1. Create a test Post instance.
2. Verify that the title of the Post matches the expected value.

**Expected Result:**  
The test should pass with a 100% success rate.

### Test Case: Post Model Slug 

**Objective:**  
Verify that the slug of the Post model is set correctly.

**Test Steps:**  
1. Create a test Post instance.
2. Verify that the slug of the Post matches the expected value.

**Expected Result:**  
The test should pass with a 100% success rate.

### Test Case: Post Model Absolute URL 

**Objective:**  
Ensure that the absolute URL of the Post model is generated correctly.

**Test Steps:**  
1. Create a test Post instance.
2. Get the absolute URL of the Post.
3. Compare the generated URL with the expected URL.

**Expected Result:**  
The test should pass with a 100% success rate.

## Conclusion

The automated testing conducted for the WildHook Blog App ensures the correctness and functionality of the Post model. All tests have resulted in a 100% success rate, confirming the reliability of the blog's core functionality.

<br>
<br>
<br>


# Manual Testing Guide: Introduction

Welcome to the manual testing guide for the WildHook. The following provides detailed procedures for testing various components of the application to ensure functionality, security, and user experience.

The manual testing guide is organised into sections, including models, views and user interactions. Within each section, you will find detailed instructions for setting up the test environment, executing test procedures, and validating expected outcomes.

## Overview of Testing Procedures

1. **Models Testing**: This section covers testing procedures for Django models, including creating objects, updating fields, and validating data integrity.

2. **Views Testing**: Here, you will find procedures for testing views, which handle presentation logic and user interactions. Testing includes rendering templates, processing form submissions, and handling redirects.

3. **User Interactions Testing**: This section focuses on testing user interactions, such as user authentication, access control, and user-specific actions.

By following the procedures outlined in this manual testing guide, you can ensure the reliability, security, and performance of your Django application, providing users with a seamless and satisfying experience. Let's dive into the testing procedures and ensure the robustness of our application!

## Manual Testing
## Table of Contents
1. [Blog App](#blog-app)
   - [Blog App Models](#blog-app-models)
   - [Blog App Views](#blog-app-views)
2. [Checkout App](#checkout-app)
   - [Checkout Models](#checkout-models)
   - [Checkout Views](#checkout-views)
3. [Products App](#products-app)
   - [Products Models](#products-models)
   - [Products Views](#products-views)
4. [Profiles App](#profiles-app)
   - [Profile Models](#profile-models)
   - [Profile Views](#profile-views)
5. [Reviews App](#reviews-app)
   - [Review Models](#review-models)
   - [Review Views](#review-views)
6. [User Interaction Testing](#user-interaction-testing)

# Blog App

## Blog App Models

## Introduction
The Blog app models in the Django application define the structure of blog posts, including fields for title, author, content, publication date, and metadata. This document provides a manual testing guide to ensure that the models function correctly and maintain data integrity.

## Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Blog app models
- Test data, including sample blog posts and user accounts, for comprehensive testing

## Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the Blog app models are defined in the Django project.
3. Make sure that all necessary dependencies, such as Django and any custom utilities, are installed.

## Testing Procedure

### 1. Test Post Model
- **Objective**: Verify that the Post model accurately represents blog posts and handles fields and methods correctly.
- **Steps**:
  1. Create a new blog post instance with valid data, including a title, author, content, and publication date.
  2. Confirm that the post is saved successfully and can be retrieved from the database.
  3. Check if the slug field is generated automatically based on the post title.
  4. Test scenarios with different combinations of post data, including empty fields and special characters.
  5. Validate the `save` method to ensure that slugs are generated correctly and do not conflict with existing slugs.
  6. Verify that the `get_absolute_url` method returns the correct URL for the post detail view.

### 2. Test Field Constraints
- **Objective**: Ensure that field constraints, such as choices and unique constraints, are enforced correctly.
- **Steps**:
  1. Attempt to create a post instance with invalid choices for the `tags` and `categories` fields.
  2. Verify that the model raises appropriate validation errors for invalid choices.
  3. Test scenarios with duplicate titles to validate the uniqueness constraint on the slug field.
  4. Confirm that the model prevents saving instances with duplicate slugs.
  5. Ensure that metadata fields, such as meta description and keywords, accept valid input and do not exceed maximum lengths.


## Blog Views

### Blog App Views

## Introduction
The views in the Blog app handle the presentation logic for displaying blog posts, creating, editing, and deleting posts. This document provides a manual testing guide to ensure that the views function correctly and provide the expected behavior for users.

## Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Blog app views
- Test data, including sample blog posts and user accounts, for comprehensive testing

## Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the Blog app views are defined in the Django project.
3. Make sure that all necessary dependencies, such as Django templates and forms, are installed.

## Testing Procedure

### 1. Test Post List View
- **Objective**: Verify that the post list view displays a list of all blog posts.
- **Steps**:
  1. Access the post list view URL and confirm that it renders correctly.
  2. Check if all existing blog posts are listed on the page.
  3. Validate the layout and styling of the post list view, ensuring readability and usability.
  4. Test scenarios with different numbers of blog posts, including empty and populated lists.
  5. Verify that pagination, if implemented, works correctly for large numbers of blog posts.

### 2. Test Post Detail View
- **Objective**: Ensure that the post detail view shows a detailed view of a single blog post.
- **Steps**:
  1. Access the post detail view URL for a specific blog post and confirm that it renders correctly.
  2. Validate that the content of the blog post, including title, author, publication date, and content, is displayed accurately.
  3. Test scenarios with different types of blog posts, including posts with images and varying lengths of content.
  4. Check if metadata, such as meta keywords and description, is displayed correctly.
  5. Ensure that the post detail view handles non-existent or invalid URLs gracefully, displaying appropriate error messages.

### 3. Test Create Post View
- **Objective**: Verify that the create post view allows superusers to create new blog posts.
- **Steps**:
  1. Log in as a superuser and access the create post view URL.
  2. Fill out the post creation form with valid data and submit it.
  3. Confirm that the new blog post is created successfully and added to the database.
  4. Test scenarios with different combinations of post data, including empty fields and file uploads.
  5. Verify that non-superusers are redirected to the post list view and cannot access the create post view.

### 4. Test Edit Post View
- **Objective**: Ensure that the edit post view allows superusers to modify existing blog posts.
- **Steps**:
  1. Log in as a superuser and access the edit post view URL for an existing blog post.
  2. Modify the post content using the edit form and save the changes.
  3. Confirm that the changes are reflected in the updated blog post.
  4. Test scenarios with different types of edits, including changes to title, content, and metadata.
  5. Validate that non-superusers are redirected and cannot access the edit post view.

### 5. Test Delete Post View
- **Objective**: Verify that the delete post view allows superusers to delete existing blog posts.
- **Steps**:
  1. Log in as a superuser and access the delete post view URL for an existing blog post.
  2. Confirm the deletion action and verify that the blog post is removed from the database.
  3. Test scenarios with different types of posts, including posts with comments and metadata.
  4. Validate that non-superusers are redirected and cannot access the delete post view.

<br>
<br>


# Checkout App
## Checkout Models
### Checkout App Models

## Introduction
The models in the Checkout app manage customer orders, including order details and line items. This document provides a manual testing guide to ensure that the models function correctly, calculate order totals accurately, and maintain data integrity.

## Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Checkout app models
- Test data, including sample products and user profiles, for comprehensive testing

## Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the Checkout app models are defined in the Django project.
3. Make sure that all necessary dependencies, such as Django settings and related models, are configured properly.

## Testing Procedure

### 1. Test Order Model
- **Objective**: Verify that the Order model correctly stores customer order information.
- **Steps**:
  1. Create a new order object with sample data, including user profile, delivery details, and line items.
  2. Check that the order number is generated automatically and is unique.
  3. Validate the calculation of order totals, including order total, delivery cost, and grand total.
  4. Test scenarios with different combinations of order data, including empty and populated fields.
  5. Ensure that the save method overrides work as expected, setting the order number and updating totals.

### 2. Test OrderLineItem Model
- **Objective**: Ensure that the OrderLineItem model accurately represents product and quantity information for each order.
- **Steps**:
  1. Create a new order line item object with sample data, including order reference, product details, and quantity.
  2. Validate that the line item total is calculated correctly based on the product price and quantity.
  3. Test scenarios with different product sizes and quantities, including edge cases and boundary conditions.
  4. Ensure that the save method overrides work as expected, setting the line item total and updating the order total.
  5. Check that the string representation of the order line item includes relevant information, such as product SKU and order number.

## Checkout Views
### Introduction
The views in the Checkout app handle the checkout process, including order submission, payment processing, and order success pages. This document provides a manual testing guide to ensure that the views function correctly, process payments securely, and display appropriate messages to users.

### Prerequisites
- Django environment with the Checkout app installed
- Test data, including sample products and user profiles, for comprehensive testing
- Access to the Stripe test environment for payment processing testing

### Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the Stripe test environment is configured correctly with valid test API keys.
3. Make sure that all necessary dependencies, such as Django settings and related views, are configured properly.

### Testing Procedure

### 1. Test `cache_checkout_data` View
- **Objective**: Verify that customer information is saved securely during the checkout process.
- **Steps**:
  1. Simulate a POST request to the `cache_checkout_data` endpoint with valid data, including the client secret.
  2. Check that the function successfully modifies the Stripe PaymentIntent metadata.
  3. Ensure that the appropriate HTTP status code (200) is returned for successful processing.
  4. Test error handling by providing invalid data or encountering exceptions and verify that error messages are displayed correctly.

### 2. Test `checkout` View
- **Objective**: Ensure that the checkout page is rendered correctly and handles the payment process securely.
- **Steps**:
  1. Access the checkout page URL and verify that the page loads without errors.
  2. Test scenarios with different combinations of bag contents, including empty and populated bags.
  3. Check that the order form is displayed correctly with pre-filled user information for authenticated users.
  4. Simulate a POST request to the `checkout` endpoint with valid form data and verify that the order is processed correctly.
  5. Test scenarios with invalid form data and ensure that appropriate error messages are displayed.
  6. Validate the integration with the Stripe payment gateway by simulating successful and failed payment attempts.
  7. Test scenarios with missing or invalid Stripe API keys and ensure that appropriate warning messages are displayed.

### 3. Test `checkout_success` View
- **Objective**: Verify that the checkout success page is displayed correctly after successful order processing.
- **Steps**:
  1. Access the checkout success page URL with a valid order number and verify that the page loads without errors.
  2. Test scenarios with different combinations of order data, including orders with and without associated user profiles.
  3. Ensure that the order details are displayed accurately on the success page, including the order number and customer information.
  4. Validate that the confirmation message is displayed correctly and includes the order number.
  5. Test scenarios with and without items in the session bag and ensure that the bag is cleared after successful checkout.



# Products App
## Product Model

### Introduction
The Product model in the Django application represents individual products available for sale. This document outlines the steps for manual testing to ensure that the Product model functions correctly and maintains data integrity.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Product model
- Sample data, including categories and products, for comprehensive testing

### Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the Product model is defined in the Django project.
3. Make sure that all necessary dependencies, such as Django settings and related models, are configured properly.

### Testing Procedure

1. **Test Product Creation**
   - **Objective**: Verify that products can be created with valid data.
   - **Steps**: 
      1. Using the Django admin interface or management commands, create a new product with valid data for all required fields.
      2. Check that the product is saved successfully in the database without any errors.
      3. Verify that all fields, including name, description, price, and category, are stored correctly.
      4. Test scenarios with different combinations of optional fields, such as offer price, label, and tag.

2. **Test Product Modification**
   - **Objective**: Ensure that existing products can be updated with new information.
   - **Steps**: 
      1. Retrieve an existing product from the database using the Django admin interface or management commands.
      2. Modify one or more fields of the product, such as price, description, or image.
      3. Save the changes and verify that the product is updated successfully without any errors.
      4. Check that the modified fields reflect the updated information in the database.

3. **Test Product Deletion**
   - **Objective**: Confirm that products can be deleted without errors.
   - **Steps**: 
      1. Identify an existing product in the database that is no longer needed for testing.
      2. Delete the product using the Django admin interface or management commands.
      3. Verify that the product is removed from the database without any errors.
      4. Ensure that any associated data, such as images or related records, are also deleted or updated accordingly.

4. **Test Field Constraints**
   - **Objective**: Ensure that field constraints, such as choices and maximum lengths, are enforced correctly.
   - **Steps**: 
      1. Attempt to create a product instance with invalid choices for label and tag fields.
      2. Verify that the model raises appropriate validation errors for invalid choices.
      3. Test scenarios with different lengths of name, description, and SKU fields to validate maximum lengths.
      4. Confirm that the model prevents saving instances with excessively long values and raises validation errors.

5. **Test Image Upload**
   - **Objective**: Verify that product images can be uploaded and associated with products.
   - **Steps**: 
      1. Create a new product or select an existing product for testing.
      2. Upload an image file using the Django admin interface or management commands.
      3. Verify that the image is associated with the product and stored correctly in the media directory.
      4. Test scenarios with different image formats, sizes, and aspect ratios to ensure compatibility and proper handling.

## Category Model

### Introduction
The Category model in the Django application represents product categories to organize and classify products. This document outlines the steps for manual testing to ensure that the Category model functions correctly and maintains data integrity.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Category model
- Sample data, including categories and products, for comprehensive testing

### Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the Category model is defined in the Django project.
3. Make sure that all necessary dependencies, such as Django settings and related models, are configured properly.

### Testing Procedure

1. **Test Category Creation**
   - **Objective**: Verify that categories can be created with valid data.
   - **Steps**: 
      1. Using the Django admin interface or management commands, create a new category with a unique name.
      2. Check that the category is saved successfully in the database without any errors.
      3. Verify that the name and friendly name fields are stored correctly.
      4. Test scenarios with different combinations of optional fields, such as friendly name.

2. **Test Category Modification**
   - **Objective**: Ensure that existing categories can be updated with new information.
   - **Steps**: 
      1. Retrieve an existing category from the database using the Django admin interface or management commands.
      2. Modify the name or friendly name field of the category.
      3. Save the changes and verify that the category is updated successfully without any errors.
      4. Check that the modified fields reflect the updated information in the database.

3. **Test Category Deletion**
   - **Objective**: Confirm that categories can be deleted without errors.
   - **Steps**: 
      1. Identify an existing category in the database that is no longer needed for testing.
      2. Delete the category using the Django admin interface or management commands.
      3. Verify that the category is removed from the database without any errors.
      4. Ensure that any associated data, such as related products, are also deleted or updated accordingly.

## Product Views


## All Products View

### Introduction
The All Products view in the Django application displays a list of all available products and allows users to filter products by category and search for specific items. This document outlines the steps for manual testing to ensure that the All Products view functions correctly and provides the expected behavior for users.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Product views
- Test data, including product categories and items, for comprehensive testing

### Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the Product views are defined in the Django project.
3. Make sure that all necessary dependencies, such as Django templates and forms, are installed.

### Testing Procedure

1. **Test Product Filtering by Category**
   - **Objective**: Verify that users can filter products by category.
   - **Steps**: 
      1. Access the All Products page and observe the list of available products.
      2. Select one or more categories from the category filter dropdown menu.
      3. Confirm that the list of products is updated dynamically to display only products belonging to the selected categories.
      4. Test scenarios with different combinations of selected categories and verify that the filter works as expected.

2. **Test Product Search**
   - **Objective**: Ensure that users can search for specific products using keywords.
   - **Steps**: 
      1. Access the All Products page and locate the search bar.
      2. Enter a keyword or phrase related to the desired product into the search bar.
      3. Submit the search query and observe the list of products displayed.
      4. Confirm that the search results include products whose names or descriptions contain the entered keyword(s).
      5. Test scenarios with different search queries, including single and multiple keywords, to validate search accuracy.

3. **Test Product Display**
   - **Objective**: Verify that all available products are displayed correctly with relevant information.
   - **Steps**: 
      1. Access the All Products page and observe the list of available products.
      2. Verify that each product card displays essential information, such as name, price, and category.
      3. Check that product images, if available, are displayed correctly and aligned with their respective product cards.
      4. Test scenarios with different numbers of products, including empty and populated lists, to ensure consistent display.

4. **Test Error Handling**
   - **Objective**: Ensure that error messages are displayed appropriately for invalid user inputs.
   - **Steps**: 
      1. Attempt to filter products by selecting non-existent categories from the category filter dropdown menu.
      2. Verify that the view handles the invalid input gracefully and displays a user-friendly error message.
      3. Test scenarios with empty search queries or invalid search terms and confirm that error messages are displayed as expected.

## Product Detail View

### Introduction
The Product Detail view in the Django application displays detailed information about a specific product, including its name, description, price, and category. This document outlines the steps for manual testing to ensure that the Product Detail view functions correctly and provides accurate information to users.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Product views
- Test data, including product categories and items, for comprehensive testing

### Testing Procedure

1. **Test Product Detail Display**
   - **Objective**: Verify that the Product Detail view displays accurate information about the selected product.
   - **Steps**: 
      1. Access the Product Detail page for a specific product.
      2. Verify that the product's name, description, price, category, and any other relevant information are displayed correctly.
      3. Check that the product image, if available, is displayed prominently and aligned with the product details.
      4. Test scenarios with different products, including products with and without images, to ensure consistent display.

2. **Test Error Handling**
   - **Objective**: Ensure that appropriate error messages are displayed for invalid product IDs or non-existent products.
   - **Steps**: 
      1. Attempt to access the Product Detail page with an invalid product ID or a non-existent product.
      2. Verify that the view handles the invalid input gracefully and displays a user-friendly error message.
      3. Test scenarios with different types of invalid product IDs to validate error handling robustness.

## Add Product View

### Introduction
The Add Product view in the Django application allows authorized users to add new products to the store. This document outlines the steps for manual testing to ensure that the Add Product view functions correctly and securely adds products to the database.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Product views
- Superuser privileges or access to an account with permission to add products

### Testing Procedure

1. **Test Add Product Form Display**
   - **Objective**: Verify that the Add Product form is displayed correctly on the Add Product page.
   - **Steps**: 
      1. Log in to the Django application with a user account that has permission to add products.
      2. Access the Add Product page and observe the layout and structure of the Add Product form.
      3. Check that all required fields, such as product name, description, and price, are included in the form.
      4. Test scenarios with different browsers and screen sizes to ensure responsive design.

2. **Test Add Product Form Submission**
   - **Objective**: Ensure that new products can be added to the store database via the Add Product form.
   - **Steps**: 
      1. Fill out the Add Product form with valid information for all required fields.
      2. Submit the form and verify that the product is added to the database successfully without any errors.
      3. Check that a success message is displayed to confirm the successful addition of the product.
      4. Test scenarios with different combinations of form data, including empty and populated fields, to validate form submission.

3. **Test Access Control**
   - **Objective**: Verify that only authorized users with superuser privileges can access the Add Product page.
   - **Steps**: 
      1. Attempt to access the Add Product page without logging in or with a non-superuser account.
      2. Verify that unauthorized access is denied, and the user is redirected to the login page or homepage.
      3. Test scenarios with different user roles and permissions to ensure access control effectiveness.

## Edit Product View

### Introduction
The Edit Product view in the Django application allows authorized users to modify existing products in the store. This document outlines the steps for manual testing to ensure that the Edit Product view functions correctly and securely updates products in the database.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Product views
- Superuser privileges or access to an account with permission to edit products

### Testing Procedure

1. **Test Edit Product Form Display**
   - **Objective**: Verify that the Edit Product form is displayed correctly on the Edit Product page.
   - **Steps**: 
      1. Log in to the Django application with a user account that has permission to edit products.
      2. Access the Edit Product page for a specific product and observe the layout and structure of the Edit Product form.
      3. Check that all relevant product information, including name, description, and price, is pre-populated in the form.
      4. Test scenarios with different browsers and screen sizes to ensure responsive design.

2. **Test Edit Product Form Submission**
   - **Objective**: Ensure that existing products can be updated in the store database via the Edit Product form.
   - **Steps**: 
      1. Modify one or more fields of the Edit Product form with updated information for the selected product.
      2. Submit the form and verify that the product is updated in the database successfully without any errors.
      3. Check that a success message is displayed to confirm the successful update of the product.
      4. Test scenarios with different combinations of form data, including empty and populated fields, to validate form submission.

3. **Test Access Control**
   - **Objective**: Verify that only authorized users with superuser privileges can access the Edit Product page.
   - **Steps**: 
      1. Attempt to access the Edit Product page without logging in or with a non-superuser account.
      2. Verify that unauthorized access is denied, and the user is redirected to the login page or homepage.
      3. Test scenarios with different user roles and permissions to ensure access control effectiveness.

## Delete Product View

### Introduction
The Delete Product view in the Django application allows authorized users to delete existing products from the store. This document outlines the steps for manual testing to ensure that the Delete Product view functions correctly and securely removes products from the database.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Product views
- Superuser privileges or access to an account with permission to delete products

### Testing Procedure

1. **Test Delete Product Confirmation**
   - **Objective**: Verify that users are prompted for confirmation before deleting a product.
   - **Steps**: 
      1. Log in to the Django application with a user account that has permission to delete products.
      2. Access the Delete Product page for a specific product and observe the confirmation prompt.
      3. Confirm that the confirmation prompt includes relevant information about the product to be deleted.
      4. Test scenarios with different browsers and screen sizes to ensure responsive design.

2. **Test Delete Product Functionality**
   - **Objective**: Ensure that products can be deleted from the store database securely.
   - **Steps**: 
      1. Confirm the deletion of the selected product by clicking the delete button in the confirmation prompt.
      2. Verify that the product is removed from the database successfully without any errors.
      3. Check that a success message is displayed to confirm the successful deletion of the product.
      4. Test scenarios with different products, including products with associated data, to validate deletion functionality.

3. **Test Access Control**
   - **Objective**: Verify that only authorized users with superuser privileges can access the Delete Product page.
   - **Steps**: 
      1. Attempt to access the Delete Product page without logging in or with a non-superuser account.
      2. Verify that unauthorized access is denied, and the user is redirected to the login page or homepage.
      3. Test scenarios with different user roles and permissions to ensure access control effectiveness.


# Profiles App
## Profile Models 
### Introduction
The UserProfile model is designed to store additional information about users in the Django application, such as delivery information and order history. This document outlines the steps for manual testing to ensure that the UserProfile model functions correctly.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the UserProfile model

### Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the UserProfile model is defined in the Django project.
3. Make sure that all necessary dependencies, such as Django and django-countries, are installed.

### Testing Procedure

### 1. Create a UserProfile Object
- **Objective**: Verify that a UserProfile object can be created successfully.
- **Steps**:
  1. Use the Django shell or an admin interface to create a new User object.
  2. Verify that a corresponding UserProfile object is automatically created for the user.
  3. Check that the UserProfile object contains the correct default values for each field.

### 2. Update a UserProfile Object
- **Objective**: Ensure that an existing UserProfile object can be updated successfully.
- **Steps**:
  1. Retrieve an existing User object from the database.
  2. Modify one or more fields in the associated UserProfile object.
  3. Save the UserProfile object and verify that the changes are reflected in the database.
  4. Check that the modified fields in the UserProfile object have been updated correctly.

### 3. Delete a UserProfile Object
- **Objective**: Confirm that a UserProfile object can be deleted without errors.
- **Steps**:
  1. Identify an existing User object with an associated UserProfile.
  2. Delete the UserProfile object.
  3. Verify that the UserProfile object is removed from the database.
  4. Ensure that the associated User object remains unaffected by the deletion of the UserProfile.

### 4. Signal Handling
- **Objective**: Test the signal handling functionality to ensure that a UserProfile object is created or updated automatically when a User object is saved.
- **Steps**:
  1. Create a new User object.
  2. Verify that a corresponding UserProfile object is automatically created.
  3. Update the User object and save the changes.
  4. Confirm that the associated UserProfile object is updated accordingly.
  5. Test edge cases, such as creating or updating a User object without triggering the signal handler.

### 5. Boundary Testing
- **Objective**: Check for boundary conditions and edge cases to ensure that the UserProfile model handles them gracefully.
- **Steps**:
  - Test scenarios such as:
    - Creating a UserProfile object with all fields filled.
    - Creating a UserProfile object with empty or null values for optional fields.
    - Providing invalid input for fields, such as non-numeric characters in phone numbers or invalid country codes.
    - Testing performance with a large number of UserProfile objects.
<br>
<br>

## Profile Views
### Introduction
The profiles views in the Django application handle user profile-related functionalities, such as displaying and updating user profiles and viewing order history. This document outlines the steps for manual testing to ensure that the profiles views function correctly.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the profiles views
- Test user accounts with associated profiles and orders in the database

### Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the profiles views are defined in the Django project.
3. Make sure that all necessary dependencies, such as Django and any custom forms, are installed.

### Testing Procedure

### 1. Test Profile View
- **Objective**: Verify that the profile view displays the user's profile correctly and allows for profile updates.
- **Steps**:
  1. Log in to the Django application with a test user account.
  2. Access the profile page and verify that the user's profile information is displayed correctly.
  3. Check if the profile form allows for updates to the user's profile.
  4. Submit the form with valid data and verify that the profile is updated successfully.
  5. Submit the form with invalid data and confirm that appropriate error messages are displayed.
  6. Test edge cases, such as updating the profile with different combinations of input values and field validations.

### 2. Test Order History View
- **Objective**: Ensure that the order history view displays past orders correctly.
- **Steps**:
  1. Log in to the Django application with a test user account.
  2. Access the order history page and verify that past orders are listed.
  3. Click on a specific order to view detailed information.
  4. Confirm that the order details are displayed accurately, including order number and items.
  5. Test scenarios with different orders, including orders with multiple items and orders with special characters in the order number.
  6. Verify that the confirmation message indicates the order number and the existence of a confirmation email.

### 3. Test Access Control
- **Objective**: Ensure that the views are protected and accessible only to authenticated users.
- **Steps**:
  1. Attempt to access the profile and order history pages without logging in.
  2. Verify that unauthorized access redirects to the login page.
  3. Log in with a valid user account and confirm that access to the profile and order history pages is granted.
  4. Test scenarios with different user roles and permissions, if applicable.


# Reviews App
## Review Models

### Introduction
The Review model in the Django application represents user reviews for products, including ratings and comments. This document outlines the steps for manual testing to ensure that the Review model functions correctly and maintains data integrity.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the Review model
- Test data, including user accounts, products, and reviews, for comprehensive testing

### Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the Review model is defined in the Django project.
3. Make sure that all necessary dependencies, such as Django user models and product models, are properly configured.

### Testing Procedure

1. **Test Review Creation**
   - **Objective**: Verify that users can create new reviews for products.
   - **Steps**: 
      1. Access the Django admin interface or the application's review creation page.
      2. Select a product for which to create a review.
      3. Enter a rating value between 1 and 5 for the selected product.
      4. Write a comment describing the user's experience with the product.
      5. Submit the review form and verify that the review is created successfully.
      6. Test scenarios with different products, ratings, and comments to validate review creation functionality.

2. **Test Review Display**
   - **Objective**: Ensure that reviews are displayed correctly with relevant information.
   - **Steps**: 
      1. Access the product detail page for a specific product.
      2. Verify that all user reviews for the product are displayed prominently.
      3. Check that each review includes the user's name, rating, comment, and creation date.
      4. Test scenarios with products having multiple reviews to ensure consistent display.

3. **Test Review Editing**
   - **Objective**: Verify that users can edit their own reviews or superusers can edit any review.
   - **Steps**: 
      1. Log in to the Django application with a user account that has permission to edit reviews.
      2. Access the review detail page for a specific review.
      3. If the user is the author of the review or a superuser, locate the edit button.
      4. Click the edit button and modify the rating and/or comment as desired.
      5. Submit the updated review form and verify that the review is edited successfully.
      6. Test scenarios with different user roles and permissions to validate review editing functionality.

4. **Test Review Deletion**
   - **Objective**: Ensure that users can delete their own reviews or superusers can delete any review.
   - **Steps**: 
      1. Log in to the Django application with a user account that has permission to delete reviews.
      2. Access the review detail page for a specific review.
      3. If the user is the author of the review or a superuser, locate the delete button.
      4. Click the delete button and confirm the deletion when prompted.
      5. Verify that the review is removed from the database successfully.
      6. Test scenarios with different user roles and permissions to validate review deletion functionality.

5. **Test User Access Control**
   - **Objective**: Verify that only authorized users can edit or delete reviews.
   - **Steps**: 
      1. Attempt to edit or delete a review without logging in or with a non-authorized user account.
      2. Verify that unauthorized access is denied, and the user is redirected to the login page or homepage.
      3. Test scenarios with different user roles and permissions to ensure access control effectiveness.

6. **Test Rating Field Constraints**
   - **Objective**: Ensure that the rating field only accepts values between 1 and 5.
   - **Steps**: 
      1. Attempt to create a review with a rating value less than 1 or greater than 5.
      2. Verify that the model raises appropriate validation errors for invalid rating values.
      3. Test scenarios with boundary values (1 and 5) to ensure that they are accepted as valid ratings.

7. **Test Comment Length Constraint**
   - **Objective**: Verify that the comment field enforces a maximum length constraint.
   - **Steps**: 
      1. Attempt to create a review with a comment exceeding the maximum allowed length.
      2. Verify that the model raises appropriate validation errors for comments that exceed the maximum length.
      3. Test scenarios with comments of various lengths, including the maximum allowed length, to validate constraint enforcement.

8. **Test Auto-Creation of Created At Field**
   - **Objective**: Ensure that the created_at field is automatically populated with the current date and time.
   - **Steps**: 
      1. Create a new review without explicitly setting the value of the created_at field.
      2. Verify that the created_at field is populated with the current date and time when the review is saved.
      3. Test scenarios with reviews created at different times to ensure accurate timestamping.

9. **Test User Can Edit Method**
   - **Objective**: Verify that the user_can_edit method correctly determines whether a user can edit a review.
   - **Steps**: 
      1. Test the user_can_edit method with different user objects, including the review's author and other users.
      2. Verify that the method returns True if the user is the author of the review or a superuser.
      3. Test scenarios with non-authorized users to ensure that the method returns False as expected.

10. **Test String Representation**
    - **Objective**: Ensure that the string representation of a review includes relevant information.
    - **Steps**: 
      1. Create a review object and retrieve its string representation.
      2. Verify that the string representation contains the username of the review's author and the name of the reviewed product.
      3. Test scenarios with different usernames and product names to ensure accurate string representation.


## Review Views


### Introduction
The views in the Django application handle user interactions with reviews, including adding, editing, and deleting reviews for products. This document outlines the steps for manual testing to ensure that the review views function correctly and provide the expected behavior for users.

### Prerequisites
- Python environment with Django installed
- Access to the Django project containing the review views
- Test data, including user accounts, products, and reviews, for comprehensive testing

### Test Environment Setup
1. Ensure that the Django project is set up and running correctly.
2. Verify that the review views are defined in the Django project.
3. Make sure that all necessary dependencies, such as Django user models, product models, and review models, are properly configured.
4. Ensure that user authentication and authorization mechanisms are in place.

### Testing Procedure

1. **Test Adding a Review**
   - **Objective**: Verify that users can add new reviews for products.
   - **Steps**: 
      1. Log in to the Django application with a user account.
      2. Access the product detail page for a specific product.
      3. Locate the section for adding a review and fill out the review form with a rating and comment.
      4. Submit the review form and verify that the review is added successfully.
      5. Test scenarios with different products and user accounts to validate review creation functionality.

2. **Test Editing a Review**
   - **Objective**: Ensure that users can edit their own reviews or superusers can edit any review.
   - **Steps**: 
      1. Log in to the Django application with a user account that has permission to edit reviews.
      2. Access the product detail page for a specific product containing the review to be edited.
      3. Locate the edit button next to the review and click it.
      4. Modify the rating and/or comment as desired in the review edit form.
      5. Submit the updated review form and verify that the review is edited successfully.
      6. Test scenarios with different user roles and permissions to validate review editing functionality.

3. **Test Deleting a Review**
   - **Objective**: Verify that users can delete their own reviews or superusers can delete any review.
   - **Steps**: 
      1. Log in to the Django application with a user account that has permission to delete reviews.
      2. Access the product detail page for a specific product containing the review to be deleted.
      3. Locate the delete button next to the review and click it.
      4. Confirm the deletion when prompted and verify that the review is removed from the database.
      5. Test scenarios with different user roles and permissions to validate review deletion functionality.

4. **Test User Access Control**
   - **Objective**: Ensure that only authorized users can edit or delete reviews.
   - **Steps**: 
      1. Attempt to edit or delete a review without logging in or with a non-authorized user account.
      2. Verify that unauthorized access is denied, and the user is redirected to the login page or homepage.
      3. Test scenarios with different user roles and permissions to ensure access control effectiveness.

5. **Test Form Validation**
   - **Objective**: Validate form submission and field validation for adding and editing reviews.
   - **Steps**: 
      1. Attempt to submit the review form with missing required fields (e.g., rating or comment).
      2. Verify that appropriate error messages are displayed, prompting the user to fill in the required fields.
      3. Test scenarios with invalid input values (e.g., non-numeric characters in the rating field) to validate field-level validation.
      4. Ensure that form submission is blocked if validation errors occur.

6. **Test Redirects After Actions**
   - **Objective**: Verify that users are redirected to the appropriate pages after adding, editing, or deleting reviews.
   - **Steps**: 
      1. Add a review, edit an existing review, or delete a review.
      2. Verify that the user is redirected back to the product detail page for the relevant product after the action is completed successfully.
      3. Test scenarios with different review actions to ensure correct redirection behavior.

7. **Test Error Handling**
   - **Objective**: Ensure that appropriate error messages are displayed when errors occur during review actions.
   - **Steps**: 
      1. Attempt to perform review actions (add, edit, delete) with invalid or unauthorized user accounts.
      2. Verify that error messages are displayed, informing the user of the issue (e.g., unauthorized access or form validation errors).
      3. Test scenarios with different error conditions to ensure that error messages are accurate and helpful for troubleshooting.

8. **Test User Interface**
   - **Objective**: Validate the user interface for adding, editing, and deleting reviews.
   - **Steps**: 
      1. Assess the design and layout of the review forms for adding and editing reviews.
      2. Verify that the forms are user-friendly and intuitive, with clear labels and instructions.
      3. Test scenarios with different screen sizes and devices to ensure responsiveness and compatibility.
      4. Ensure that buttons and links are clearly visible and functional for all review actions.

9. **Test Review Display**
   - **Objective**: Ensure that reviews are displayed correctly on product detail pages.
   - **Steps**: 
      1. Access the product detail page for a specific product containing multiple reviews.
      2. Verify that all reviews for the product are displayed prominently and legibly.
      3. Check that each review includes the user's name, rating, comment, and creation date.
      4. Test scenarios with products having various numbers of reviews to ensure consistent display and layout.

10. **Test Integration with Product Detail Page**
    - **Objective**: Validate the integration of review functionality with the product detail page.
    - **Steps**: 
      1. Verify that the product detail page includes sections for displaying and interacting with reviews.
      2. Test the functionality of buttons or links for adding, editing, and deleting reviews directly from the product detail page.
      3. Ensure that reviews are updated dynamically without page refresh when new reviews are added or existing reviews are edited or deleted.
      4. Test scenarios with different product detail pages and review interactions to ensure seamless integration.

11. **Test Review Form Pre-filling for Editing**
    - **Objective**: Verify that the review form is pre-filled with existing review data when editing a review.
    - **Steps**: 
      1. Access the edit page for a specific review.
      2. Verify that the review form is pre-filled with the existing rating and comment for the review.
      3. Test scenarios with different reviews to ensure that the correct review data is pre-filled for editing.



## User Interaction Testing

This section focuses on testing user interactions within the WildHook application. User interactions test functionalities that users perform while using with WildHook. The primary objectives of user interactions testing include:

### Products Section Testing:

1. **Product Listing Testing**:
   - **Verification of Product Display**: Ensured that all products are correctly listed on the products page by comparing the displayed products with the ones stored in the database.
   - **Visual Inspection**: Checked the visual presentation of product images, names, descriptions, and prices to confirm they match the expected design and layout.
   - **Clickable Products**: Clicked on each product to confirm that users are redirected to the corresponding product detail page.

2. **Product Detail Testing**:
   - **Content Verification**: Verified that the product detail page displays accurate and complete information about the selected product, including description, price, and available sizes (if applicable).
   - **Functionality Testing**: Tested the functionality to select the quantity and size of the product, ensuring that the user input is properly captured.
   - **Add to Cart Testing**: Clicked on the "Add to Cart" button to ensure that the product is successfully added to the shopping cart.

### Checkout Section Testing:

1. **Shipping and Payment Details Testing**:
   - **Checkout Process Testing**: Completed the checkout process by providing shipping and payment details, and confirmed that no errors occurred during submission.
   - **Stripe Integration Testing**: Verified that the integration with Stripe for processing payments functions correctly and securely.
   - **Cart Modification Testing**: Tested the ability to add, update, or remove items from the shopping cart during the checkout process without encountering any issues.

2. **Quantity Adjustment Testing**:
   - **Quantity Increment/Decrement Testing**: Attempted to increment and decrement the quantity of each item in the shopping cart, and verified that the total order amount was updated accordingly.
   - **Validation Testing**: Ensured that users cannot add a negative quantity or exceed the available stock, and that appropriate error messages are displayed if validation fails.

### Profile Section Testing:

1. **User Profile Testing**:
   - **Shipping Information Testing**: Updated the user profile with new shipping information and confirmed that the changes were saved correctly.
   - **Profile View Testing**: Accessed the user profile page to view the stored shipping information and ensured it was displayed accurately.
   - **Form Validation Testing**: Tested the profile update form with invalid input to verify that appropriate validation messages were shown.

2. **Order History Testing**:
   - **Order Display Testing**: Checked the display of past orders in the user profile to ensure that all relevant information, such as order number, items, and total amount, was shown correctly.
   - **Order Detail View Testing**: Clicked on individual orders to view detailed information and confirmed that the order details matched the expected data.

### Reviews Section Testing:

1. **Adding Reviews Testing**:
   - **Review Submission Testing**: Logged in as a user and submitted reviews for different products to test the review submission process.
   - **Review Association Testing**: Checked that each review was associated with the correct product and user by inspecting the database entries.

2. **Editing and Deleting Reviews Testing**:
   - **Review Editing Testing**: Attempted to edit existing reviews and confirmed that only the review owner or superusers could make changes.
   - **Review Deletion Testing**: Tested the deletion of reviews to ensure that only the review owner or superusers could delete reviews.

### Blog Section Testing:

1. **Content Testing**:
   - **Blog Post Display Testing**: Reviewed the display of blog posts and their content to ensure readability and relevance to users.
   - **Content Verification**: Checked that the information provided in each blog post was accurate and valuable to users.

2. **Navigation Testing**:
   - **Internal Link Testing**: Clicked on internal links within blog posts to verify that they directed users to the correct pages, such as related product pages or other blog posts.
   - **Cross-Browser Testing**: Tested the blog navigation and functionality across different browsers to ensure consistency and compatibility.

By testing at each stage of the shopping experience, we aimed to identify any potential issues or discrepancies and ensure a seamless and user-friendly interaction with the application.


### Final Thoughts
A stringent and rigorous testing was carried out across all sections of the build. This could be further improved with larger test groups, stress testing the website on scale. This would uncover any weakness in the development and allow a more robust app to be developed. Furthermore full automated testing for all Apps within the project will be developed in later iterations, increasing the quality, structure and security of WildHook.
