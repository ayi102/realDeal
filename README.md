# realDeal

## Introduction
This application is designed to make basic real estate calculations.

## Inputs
There are two XML files that represent the input into the application. They are the following:

- data.xml
- equation.xml

### data.xml
The data.xml are all variables required by the equations. This can include revenue, operating expenses, etc. Currently, the expected XML items are defined in the data.xml value. Users can add as many defined XML items to specify their potential real estate investment. For example, a user can have a variety of operating expenses. In the data.xml, they can list all of the operating expenses that are specific to their potential real estate investment. Below is an example:

```
<operatingExpense name="electricity">
		<value>1.0</value>
        <type>utility</type>
</operatingExpense>

<operatingExpense name="water">
	<value>2.0</value>
	<type>utility</type>
</operatingExpense>
```

### Outputs

## Required Dependencies
- Python 3.9 or Greater
- Pip
- Pipenv

## Build

## Automated Unit Tests