%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_with doc_pdf

# no debug files
# package can not be noarch due to the missing dependencies in s390x
%define debug_package %{nil}

%global pypi_name devicely

%global _description %{expand:
Devicely is a Python package for reading, de-identifying and writing data from 
various health monitoring sensors. With devicely, you can read sensor data and 
have it easily accessible in dataframes. You can also de-identify data and write 
them back using their original data format. This makes it convenient to share 
sensor data with other researchers while mantaining people's privacy.}

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        7%{?dist}
Summary:        A Python package for reading, timeshifting and writing sensor data

License:        MIT
URL:            https://github.com/hpi-dhc/%{pypi_name}
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

# It depends on pyedflib which is not available on s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=2027046
ExcludeArch:    s390x

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  pandoc
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist nbsphinx}
BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist pypandoc}
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C sphinx latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C sphinx/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files devicely

# assertion errors - upsteam was informed
# https://github.com/hpi-dhc/devicely/issues/61
%check
%if %{with tests}
%pytest -k 'not Faros and not Empatica'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc sphinx/_build/latex/%{pypi_name}.pdf
%endif

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.1.1-6
- Rebuilt for Python 3.12

* Sat Apr 8 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-5
- Temporarily disable building docs

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.11

* Sun Dec 19 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-1
- Initial package
