%if 0%{?el9}
# likely some issue with a combination of sphinx and the theme used
# writing output... [ 12%] advanced
# Theme error:
# An error happened in rendering the page advanced.
# Reason: UndefinedError("'styles' is undefined")
%bcond_with doc
%else
%bcond_without doc
%endif

%global srcname mistune

%global common_description %{expand:
The fastest markdown parser in pure Python, inspired by marked.}

Name:           python-mistune
Version:        3.0.2
Release:        %autorelease
Summary:        Markdown parser for Python

License:        BSD-3-Clause
URL:            https://github.com/lepture/mistune
Source0:        %url/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Upstream uses tox to call nose. Instead, we'll just call pytest directly.
BuildRequires:  python3dist(pytest)

%description %{common_description}

%package -n python3-%{srcname}
Summary:        %{summary}

# Allow upgrades from Fedora 37 with python3-mistune08 to Fedora 38 with python3-mistune
# as python3-nbconvert requires mistune 2 on Fedora 38+.
# See https://bugzilla.redhat.com/2177923
# If the Fedora 37 python3-mistune08 package is ever bumped, this needs to be bumped as well!
Obsoletes:      python3-mistune08 < 0.8.4-8

%description -n python3-%{srcname} %{common_description}

%if %{with doc}
%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.
%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}

# replace shibuya theme which is not available in Fedora with sphinx read the docs theme
sed -i "s/html_theme = 'shibuya'/html_theme = 'sphinx_rtd_theme'/" docs/conf.py
sed -i "s/shibuya/sphinx-rtd-theme/" docs/requirements.txt
# unpin versions to allow newer versions available in Fedora
sed -i "s/sphinx==6.2.1/sphinx>=6.2.1/" docs/requirements.txt
sed -i "s/sphinx-design==0.4.1/sphinx-design<0.7.0/" docs/requirements.txt

%generate_buildrequires
%if %{with doc}
%pyproject_buildrequires docs/requirements.txt
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%if %{with doc}
# generate html docs
PYTHONPATH=$PWD/build/lib sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{srcname}

%{_fixperms} %{buildroot}/*

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%if %{with doc}
%files doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
