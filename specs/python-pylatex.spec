# Enabled by default
# If the package needs to download data for the test which cannot be done in
# koji, these can be disabled in koji by using `bcond_with` instead, but the
# tests must be validated in mock with network enabled like so:
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enable-network --with tests

# Tested for 1.4.2: all tests and examples pass
%bcond tests 0

# unable to use rpmautospec here---fedpkg fails to fetch sources

%global fancy_name PyLaTeX

%global _description %{expand:
PyLaTeX is a Python library for creating and compiling LaTeX files or snippets.
The goal of this library is being an easy but extensible interface between
Python and LaTeX.}

%global forgeurl https://github.com/JelteF/PyLaTeX

Name:           python-pylatex
Version:        1.4.2
Release:        4%{?dist}
Summary:        Library for creating LaTeX files and snippets

%forgemeta

# spdx
License:        MIT
URL:            https://jeltef.github.io/PyLaTeX/
Source0:        %forgesource
BuildArch:      noarch

%description %_description

%{?python_enable_dependency_generator}

%package -n python3-pylatex
Summary:        %{summary}
# Not picked up by dep generator
Requires:       %{py3_dist matplotlib}
Requires:       %{py3_dist quantities}
Requires:       %{py3_dist numpy}
# Will also pull a lot of texlive, but that cannot be helpeb
Requires:       /usr/bin/latexmk
Requires:       /usr/bin/pdflatex
# From `ag Package`
Requires:       tex(alltt.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(longtable.sty)
Requires:       tex(ltablex.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multirow.sty)
Requires:       tex(parskip.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tabu.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       texlive

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
# Explicit requirements for tests
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist quantities}
# https://fedoraproject.org/wiki/Features/TeXLive
BuildRequires:  tex(alltt.sty)
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(booktabs.sty)
BuildRequires:  tex(cleveref.sty)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(lmodern.sty)
BuildRequires:  tex(lastpage.sty)
BuildRequires:  tex(longtable.sty)
BuildRequires:  tex(ltablex.sty)
BuildRequires:  tex(mdframed.sty)
BuildRequires:  tex(microtype.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(parskip.sty)
BuildRequires:  tex(pgfplots.sty)
BuildRequires:  tex(ragged2e.sty)
BuildRequires:  tex(subcaption.sty)
BuildRequires:  tex(siunitx.sty)
BuildRequires:  tex(tabularx.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(textcomp.sty)
BuildRequires:  tex(textpos.sty)
BuildRequires:  tex(tikz.sty)
BuildRequires:  tex(xcolor.sty)
BuildRequires:  texlive
%endif

%py_provides python3-pylatex

%description -n python3-pylatex %_description

%prep
%forgesetup

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pylatex


%check
%if %{with tests}
# Run tests
%pytest

# Test examples
pushd examples
for f in *.py; do
    PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} $f
done
popd
%endif

%files -n python3-pylatex -f %{pyproject_files}
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.13

* Tue Feb 20 2024 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.2-1
- Update to latest release

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 1.4.1-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.4.1-7
- Rebuilt for Python 3.11

* Wed Mar 16 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.4.1-6
- Utilize pytest instead of the deprecated nose test runner

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.1-1
- Update to latest release

* Thu Oct 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.0-1
- Update to new release

* Sat Aug 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.4-1
- Update to new release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.3-2
- Explicitly BR setuptools

* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.3-1
- Update to 1.3.3

* Mon Jun 15 2020 Victor Tejada Yau <victortyau@gmail.com> 1.3.2-1
- Update to 1.3.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.1-1
- Update to 1.3.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.0-1
- Minor tweaks as per review comments
- https://bugzilla.redhat.com/show_bug.cgi?id=1721409
- Improve description macro

* Mon Jun 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.0-1
- Initial rpm build
