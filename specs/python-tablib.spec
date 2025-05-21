%bcond_with bootstrap

Name:             python-tablib
Version:          3.8.0
Release:          %autorelease
Summary:          Format agnostic tabular data library (XLS, JSON, YAML, CSV, etc.)

License:          MIT
URL:              http://github.com/jazzband/tablib
Source:           %{pypi_source tablib}

BuildArch:        noarch

BuildRequires:  python3-devel
# documentation
%if %{without bootstrap}
BuildRequires:  make
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist tablib}
BuildRequires:  texinfo
%endif
# test requirements
BuildRequires:  %{py3_dist pytest}

%global _description %{expand: \
Tablib is a format-agnostic tabular dataset library, written in Python.}

%description %_description

%package -n python3-tablib
Summary:        %{summary}

%if %{defined fc42} || %{defined fc41}
# For backwards-compatibility with manual Requires, keep hard dependencies on
# the corresponding extras metapackages.
Requires:       python3-tablib+ods = %{version}-%{release}
Requires:       python3-tablib+xls = %{version}-%{release}
Requires:       python3-tablib+xlsx = %{version}-%{release}
Requires:       python3-tablib+yaml = %{version}-%{release}
%endif

%description -n python3-tablib %{_description}


%pyproject_extras_subpkg -n python3-tablib cli ods pandas xls xlsx yaml
%pyproject_extras_subpkg -n python3-tablib all
%pyproject_extras_subpkg -n python3-tablib html

%prep
%autosetup -n tablib-%{version}
# Remove shebangs from non-script sources. The find-then-modify pattern
# preserves mtimes on sources that did not need to be modified.
find 'src' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/ --cov(=|-report )[^ ]+//g' pytest.ini

%generate_buildrequires
%{pyproject_buildrequires \
    -x all \
    -x cli \
    -x html \
    -x ods \
    -x pandas \
    -x xls \
    -x xlsx \
    -x yaml}

%build
%pyproject_wheel
# Build documentation
%if %{without bootstrap}
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook tablib
popd
popd
%endif

%install
%pyproject_install
%pyproject_save_files -l tablib
%if %{without bootstrap}
mkdir -p %{buildroot}/%{_datadir}/help/en/python-tablib
install -m644 docs/texinfo/tablib.xml \
  %{buildroot}/%{_datadir}/help/en/python-tablib/
%endif

%check
%pytest -v
 
%files -n python3-tablib -f %{pyproject_files}
%doc AUTHORS
%doc HISTORY.md
%doc README.md
%if %{without bootstrap}
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-tablib/
%endif

%changelog
%autochangelog
