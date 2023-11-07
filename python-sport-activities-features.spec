%bcond_without tests
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%global pypi_name sport-activities-features

%global _description %{expand:
A minimalistic toolbox for extracting features 
from sport activity files written in Python. Proposed software 
supports the extraction of following topographic features from
sport activity files: number of hills, average altitude of identified 
hills, total distance of identified hills, climbing ratio (total distance
of identified hills vs. total distance), average ascent of hills, 
total ascent, total descent and many others.}

Name:           python-%{pypi_name}
Version:        0.3.16
Release:        1%{?dist}
Summary:        A minimalistic toolbox for extracting features from sports activity files

# SPDX
License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  make

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%endif

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{pypi_name} %_description

%package -n python3-%{pypi_name}-tests
Summary:        Tests for python3-%{pypi_name}

Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
%{summary}.

%package doc
Summary:        Documentation and examples for %{name}

Requires:       python3-%{pypi_name} = %{version}-%{release}
# Used in some examples; an indirect dependency of the base package, but not a
# direct one
Requires:       %{py3_dist numpy}

%description doc
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version} -S git
rm -fv poetry.lock

#make dependencies consistent with Fedora versions
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

# Fix version in docs to match the package version:
sed -r -i 's/(release = ")[[:digit:].]+"/\1%{version}"/' docs/conf.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files sport_activities_features

%check	
%if %{with tests}
%pytest -k 'not test_overpy_node_manipulation and not test_data_analysis and not test_hill_identification and not test_missing_elevation_identification'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE

%files -n python3-%{pypi_name}-tests
%doc tests/

%files doc
# Depends on base package, which provides the LICENSE file
%doc AUTHORS.rst
%doc CHANGELOG.md
%doc CITATION.cff
%doc CODE_OF_CONDUCT.md
%doc README.md
%doc docs/preprints/A_minimalistic_toolbox.pdf
%if %{with doc_pdf}
%doc docs/_build/latex/%{pypi_name}.pdf
%endif
%doc examples/

%changelog
* Sun Nov 5 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.3.16-1
- Update to 0.3.16

* Mon Sep 11 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.3.15.1-1
- Update to 0.3.15.1

* Sat Sep 2 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.3.15-1
- Update to 0.3.15

* Fri Aug 11 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.3.14-2
- Rebuilt
- Disable one test (test_data_analysis)

* Wed Jul 26 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.3.14-1
- Update to 0.3.14

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 5 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.12-1
- Update to 0.3.12

* Mon Apr 24 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.11-2
- Enable one test

* Mon Apr 3 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.11-1
- Upgrade to 0.3.11

* Tue Mar 7 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.10-1
- Upgrade to 0.3.10

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.8-1
- Upgrade to 0.3.8

* Fri Dec 2 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.7.2-1
- Upgrade to 0.3.7.2

* Fri Oct 21 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.7.1-1
- Upgrade to 0.3.7.1

* Wed Oct 12 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.7-1
- Upgrade to 0.3.7

* Sun Aug 28 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.6-1
- Upgrade to 0.3.6

* Fri Aug 19 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.5-1
- Upgrade to 0.3.5

* Tue Aug 2 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.2-1
- Upgrade to 0.3.2
- Re-enable tests

* Mon Aug 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.1-1
- Upgrade to 0.3.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.0-1
- Update to 0.3.0

* Sat Jul 2 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.18-1
- Update to the latest upstream's release

* Wed Jun 8 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.16-1
- Update to the latest upstream's release

* Mon May 2 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.15-2
- Replace summary of package

* Tue Apr 26 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.15-1
- Update to the latest upstream's release

* Sun Feb 20 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.14-1
- Update to the latest upstream's release

* Thu Feb 3 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.12-1
- Update to the latest upstream's release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
