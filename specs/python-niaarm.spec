%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%global pypi_name niaarm
%global pretty_name NiaARM

%global _description %{expand:
NiaARM is a framework for Association Rule Mining based on nature-inspired
algorithms for optimization. The framework is written fully in Python and
runs on all platforms. NiaARM allows users to preprocess the data in a
transaction database automatically, to search for association rules and
provide a pretty output of the rules found. This framework also supports
numerical and real-valued types of attributes besides the categorical ones.
Mining the association rules is defined as an optimization problem, and
solved using the nature-inspired algorithms that come from the related
framework called NiaPy.}

Name:           python-%{pypi_name}
Version:        0.3.12
Release:        2%{?dist}
Summary:        A minimalistic framework for numerical association rule mining

# SPDX
License:        MIT

URL:            https://github.com/firefly-cpp/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

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
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{version}
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires %{?with_doc_pdf:-x docs}

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files niaarm

install -D -t '%{buildroot}%{_mandir}/man1' -m 0644 %{pypi_name}.1

%check
%if %{with tests}
%pytest -k 'not test_visualization and not test_text_mining'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_bindir}/%{pypi_name}
%license LICENSE
%doc README.md CITATION.cff
%{_mandir}/man1/%{pypi_name}.1*

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/%{pypi_name}.pdf
%endif
%doc examples/
%doc paper/
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md
%doc interest_measures.md CHANGELOG.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 1 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.12-1
- Update to 0.3.12

* Wed Jul 24 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.11-1
- Update to 0.3.11

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.10-1
- Update to 0.3.10

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.3.8-2
- Rebuilt for Python 3.13

* Thu Mar 14 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.8-1
- Update to 0.3.8

* Thu Feb 15 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.7-1
- Update to 0.3.7

* Sun Jan 28 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.6-1
- Update to 0.3.6

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild


* Mon Nov 13 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.5-4
- Install additional doc file

* Mon Nov 6 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.5-3
- Confirm License is SPDX MIT

* Mon Nov 6 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.5-2
- Install man page

* Fri Nov 3 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.5-1
- Update to 0.3.5

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.12

* Tue May 30 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.2-1
- Update to 0.3.2

* Wed Feb 15 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.1-1
- Upgrade to 0.3.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 1 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-2
- Do not test text mining suite (nltk data is missing)

* Sun Jan 1 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-1
- Upgrade to 0.2.4

* Thu Sep 29 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.1-2
- Fix tests

* Thu Sep 29 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.1-1
- Upgrade to 0.2.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.11

* Mon May 30 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-1
- Upgrade to 0.2.0

* Sun May 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.6-1
- Upgrade to 0.1.6

* Sun Apr 10 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.5-1
- Initial package
