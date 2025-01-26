%bcond tests 1

%global _description %{expand:
sklearn-genetic is a genetic feature selection module for scikit-learn.
Genetic algorithms mimic the process of natural selection to search
for optimal values of a function.}

Name:           python-sklearn-genetic
Version:        0.6.0
Release:        %autorelease
Summary:        A genetic feature selection module for scikit-learn

License:        LGPL-3.0-only
URL:            https://github.com/manuel-calzolari/sklearn-genetic
Source:         %{url}/archive/%{version}/sklearn-genetic-%{version}.tar.gz

# Adapt for fit_params renaming in scikit-learn 1.6
# https://github.com/manuel-calzolari/sklearn-genetic/pull/49
Patch:          %{url}/pull/49.patch

BuildArch:      noarch

%description %_description

%package -n python3-sklearn-genetic
Summary:        %{summary}

# Remove after Fedora 44 reaches end-of-life
Obsoletes:      python-sklearn-genetic-doc < 0.6.0-5

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-sklearn-genetic %_description

%prep
%autosetup -n sklearn-genetic-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l genetic_selection

%check
%if %{with tests}
%pytest
%endif

%files -n python3-sklearn-genetic -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
