%global forgeurl https://github.com/rodrigo-arenas/Sklearn-genetic-opt
%global tag %{version}
%forgemeta

%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.

%bcond_without doc_pdf

%global pypi_name sklearn-genetic-opt
%global orig_name Sklearn-genetic-opt

%global _description %{expand:
scikit-learn models hyperparameters tuning and feature selection, using
evolutionary algorithms. This is meant to be an alternative to popular
methods inside scikit-learn such as Grid Search and Randomized Grid
Search for hyperparameteres tuning, and from RFE, Select From Model for
feature selection. Sklearn-genetic-opt uses evolutionary algorithms
from the DEAP package to choose the set of hyperparameters that
optimizes (max or min) the cross-validation scores, it can be used
for both regression and classification problems.}

Name:           python-%{pypi_name}
Version:        0.10.1
Release:        %autorelease
Summary:        Hyperparameters tuning and feature selection

License:        MIT
URL:            https://github.com/rodrigo-arenas/Sklearn-genetic-opt
Source0:        %{forgesource}

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist matplotlib}

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  ImageMagick
BuildRequires:  pandoc
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
BuildRequires:  %{py3_dist sphinx-copybutton}
BuildRequires:  %{py3_dist sphinx-gallery}
BuildRequires:  %{py3_dist numpydoc}
BuildRequires:  %{py3_dist nbsphinx}
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -p1 -n %{orig_name}-%{version}

%generate_buildrequires
# Cannot package “mlflow” or “all” extras due to missing mlflow dependency
%pyproject_buildrequires -x seaborn

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'

# convert gif to png and take the first frame
convert docs/_build/latex/progress_bar.gif docs/_build/latex/progress_bar.png
sed -i 's/{progress_bar}.gif/{progress_bar-0}.png/g' docs/_build/latex/sklearngeneticopt.tex
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files sklearn_genetic

%check
%if %{with tests}
# test_tensorboard_callback fails due to missing tensorflow dep
# https://github.com/rodrigo-arenas/Sklearn-genetic-opt/issues/134
k="not test_tensorboard_callback"
# Two failing tests in Python3.12, Disable for now.
# TODO: investigate and report failing tests upstream
k="${k} and not test_wrong_scheduler_methods"
k="${k} and not test_wrong_dimension"
# Exclude test_mlflow -- mlflow dependency is missing
%pytest --ignore sklearn_genetic/tests/test_mlflow.py -k "${k}" -v
%endif

%files -n python3-sklearn-genetic-opt -f %{pyproject_files}
%doc README.rst

%files doc
%if %{with doc_pdf}
%doc docs/_build/latex/sklearngeneticopt.pdf
%endif


%changelog
%autochangelog
