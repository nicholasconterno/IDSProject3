# IDS Week 2 

Data visualization using pandas.

## Makefile Usage

Our `Makefile` contains several rules to simplify the development process:

- **install**: Installs the necessary dependencies from the `requirements.txt` file.
- **lint**: Runs `flake8` to lint the code inside the `src` directory.
- **test**: Executes unit tests using `pytest`.

To use the Makefile:

### Installing Dependencies

This will install all required packages from `requirements.txt`:

```bash
make install
```

### Linting the Code

To check the code quality and maintain coding standards, run:

```bash
make lint
```

### Running Tests

To execute unit tests:

```bash
make test
```

## Data Visualization

Below is the histogram showcasing the distribution of Rotten Tomatoes Percentages:

![Histogram](./histogram.png)

## Summary Statistics
                        Audience score %  Profitability  Rotten Tomatoes %  Year
            count         46.000000      46.000000          46.000000    46.000000
            mean          64.195652       5.138843          48.326087  2009.065217
            std           13.071801      10.038464          26.619170     1.436078
            min           40.000000       0.000000           3.000000  2007.000000
            25%           52.500000       1.858302          27.250000  2008.000000
            50%           62.500000       2.640843          46.500000  2009.000000
            75%           76.000000       4.977038          69.500000  2010.000000
            max           89.000000      66.934000          93.000000  2011.000000
Mean of 'Rotten Tomatoes %': 48.32608695652174\
Median of 'Rotten Tomatoes %': 46.5\
Standard Deviation of 'Rotten Tomatoes %': 26.61916965716089
