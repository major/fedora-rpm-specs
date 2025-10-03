Name:           python-junitparser
Version:        4.0.2
Release:        %autorelease
Summary:        Manipulates JUnit/xUnit Result XML files

License:        Apache-2.0
URL:            https://github.com/weiwei/junitparser
# PyPI source does not have documentation
Source:         %{url}/archive/%{version}/junitparser-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3dist(pytest)
# Documentation
BuildRequires:  graphviz
BuildRequires:  python3dist(sphinx)
BuildRequires:  texinfo

%global _description %{expand:
junitparser handles JUnit/xUnit Result XML files. Use it to parse and
manipulate existing Result XML files, or create new JUnit/xUnit result XMLs
from scratch.

FEATURES:
- Parse or modify existing JUnit/xUnit XML files
- Parse or modify non-standard or customized JUnit/xUnit XML files, by
  monkey patching existing element definitions
- Create JUnit/xUnit test results from scratch
- Merge test result XML files
- Specify XML parser. For example you can use lxml to speed things up
- Invoke from command line, or python -m junitparser}

%description %_description

%package -n     python3-junitparser
Summary:        %{summary}

%description -n python3-junitparser %_description


%prep
%autosetup -p1 -n junitparser-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook junitparser.texi
popd
popd


%install
%pyproject_install
%pyproject_save_files -l junitparser
mkdir -p %{buildroot}%{_datadir}/help/en/python-junitparser
install -p -m644 docs/texinfo/junitparser.xml \
   %{buildroot}%{_datadir}/help/en/python-junitparser

%check
%pyproject_check_import
# Tests require different console locale settings
k="${k-}${k+ and }not (Test_Locale and test_fromstring_numbers_locale_insensitive)"
%pytest -k "${k-}"

%files -n python3-junitparser -f %{pyproject_files}
%{_bindir}/junitparser
%doc README.rst
%doc CHANGELOG.md
%doc %dir  %{_datadir}/help/en
%doc %lang(en) %{_datadir}/help/en/python-junitparser

%changelog
%autochangelog
