%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.

# docs are still not ready for production in upstream's directory
%bcond_with doc_pdf

%global pypi_name ast-monitor
%global pretty_name AST-Monitor

%global _description %{expand:
AST-monitor is a low-cost and efficient embedded device for monitoring the
realization of sport training sessions that is dedicated to monitor cycling
training sessions. AST-Monitor is a part of Artificial Sport Trainer (AST)
system.}

Name:           python-%{pypi_name}
Version:        0.5.2
Release:        2%{?dist}
Summary:        AST-Monitor is a wearable Raspberry Pi computer for cyclists

License:        MIT
# if docs enabled, then use MIT and CC-BY-SA

URL:            https://github.com/firefly-cpp/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_noarch_with_unported_dependencies
#
# This package requires python3dist(pyqtwebengine).
ExclusiveArch: %{qt6_qtwebengine_arches} noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

# For qt6_qtwebengine_arches macro:
BuildRequires:  qt6-srpm-macros

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}

# optional dependency
Recommends:     python3dist(openant)

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
BuildRequires:  %{py3_dist sphinx}
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{version}
rm -fv poetry.lock
rm -rvf examples/.vscode

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

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
%pyproject_save_files ast_monitor

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CITATION.cff HARDWARE_CONFIGURATION.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/%{pypi_name}.pdf
%doc docs/preprints/2109-13334.pdf
%endif
%doc examples/
%doc CONTRIBUTING.md
%doc CITATION.cff

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 20 2024 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.5.2-1
- Update to 0.5.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Python Maint <python-maint@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.13

* Mon Mar 25 2024 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.5.0-1
- Update to 0.5.0

* Fri Feb 9 2024 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.4.3-1
- Update to 0.4.3
- Update docs

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 2 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.4.2-1
- Update to 0.4.2

* Mon Sep 11 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.4.1-1
- Update to 0.4.1

* Fri Aug 11 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.4.0-3
- Rebuilt

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 3 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.0-1
- Update to the latest release

* Wed Feb 1 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.2-1
- Update to the latest release

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 6 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.1-1
- Update to the latest release

* Sat Nov 26 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.3.0-2
- Exclude architectures that lack qtwebengine

* Thu Sep 15 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.0-1
- Update to the latest release

* Fri Aug 19 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.1-1
- Update to the latest release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 7 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.4-1
- Update to the latest release

* Tue May 3 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.3-2
- Update to the latest release

* Tue May 3 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.3-1
- Update to the latest release

* Tue Mar 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.2-1
- Initial package
