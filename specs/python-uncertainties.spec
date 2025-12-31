Name:           python-uncertainties
Version:        3.2.3
Release:        %autorelease
Summary:        Transparent calculations with uncertainties on the quantities involved

License:        BSD-3-Clause
URL:            https://github.com/lmfit/uncertainties
Source:         %{url}/archive/%{version}/uncertainties-%{version}.tar.gz
# https://github.com/lmfit/uncertainties/pull/341
Patch0:         uncertainties-3.2.3-fix-tests.patch

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(prep): -n uncertainties-%{version}
BuildOption(generate_buildrequires): -x arrays,test
BuildOption(install): -l uncertainties

%global common_description %{expand:
The uncertainties package allows calculations with values that have
uncertainties, such as (2 +/- 0.1)*2 = 4 +/- 0.2. uncertainties takes the pain
and complexity out of error propagation and calculations of values with
uncertainties.}

%description %{common_description}

%package -n     python3-uncertainties
Summary:        %{summary}

%description -n python3-uncertainties %{common_description}

%package -n     python3-uncertainties-doc
Summary:        Documentation for %{name}
BuildRequires:  python3-sphinx
BuildRequires:  %{py3_dist sphinx_copybutton}
BuildRequires:  %{py3_dist python_docs_theme}
BuildRequires:  make

%description -n python3-uncertainties-doc %{common_description}

%prep -a
sed -i 's/"pytest_codspeed",//' pyproject.toml

%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

pushd doc
make html
rm _build/html/.buildinfo
popd

%check
%pytest

%files -n python3-uncertainties -f %{pyproject_files}

%files -n python3-uncertainties-doc
%license LICENSE.txt
%doc doc/_build/html

%changelog
%autochangelog