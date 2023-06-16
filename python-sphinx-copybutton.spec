# DOCUMENTATION NOTE: We used to build the documentation, but then upstream
# started depending on sphinx-book-theme, which we do not have in Fedora.
# Packaging it would require adding about 3 dozen new packages to Fedora, which
# is more work than I want to go to for this package, which I only need to
# generate documentation for another package.

Name:           python-sphinx-copybutton
Version:        0.5.1
Release:        3%{?dist}
Summary:        Add a copy button to code cells in Sphinx docs

License:        MIT
URL:            https://sphinx-copybutton.readthedocs.io/en/latest/
Source0:        %{pypi_source sphinx-copybutton}

BuildArch:      noarch
BuildRequires:  python3-devel

# This can be removed when F38 reaches EOL
Obsoletes:      %{name}-doc < 0.3.2
Provides:       %{name}-doc = %{version}-%{release}

# the [code_style] extra is only used for checking code style of this package
# the [rtd] is only used to generate docs on readthedocs.org
# as of 0.5.0, there are no more extras

%global _description %{expand:
Sphinx-copybutton does one thing: add a little "copy" button to the
right of your code blocks.  If the code block overlaps to the right of
the text area, you can just click the button to get the whole thing.}

%description %_description

%package     -n python3-sphinx-copybutton
Summary:        %{summary}

%description -n python3-sphinx-copybutton %_description

%prep
%autosetup -n sphinx-copybutton-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_copybutton

%check
%pyproject_check_import

%files -n python3-sphinx-copybutton -f %{pyproject_files}
%doc README.md

%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jonathan Wright <jonathan@almalinux.org> - 0.5.1-1
- Update to 0.5.1 rhbz#2142964

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.11

* Sat Feb  5 2022 Jerry James <loganjerry@gmail.com> - 0.5.0-1
- Version 0.5.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul  5 2021 Jerry James <loganjerry@gmail.com> - 0.4.0-1
- Version 0.4.0

* Thu Jul  1 2021 Jerry James <loganjerry@gmail.com> - 0.3.3-1
- Version 0.3.3
- Drop -doc subpackage due to missing dependencies

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  2 2020 Jerry James <loganjerry@gmail.com> - 0.3.1-1
- Version 0.3.1

* Mon Oct  5 2020 Jerry James <loganjerry@gmail.com> - 0.3.0-4
- Explicitly BR setuptools

* Mon Sep 21 2020 Jerry James <loganjerry@gmail.com> - 0.3.0-3
- Remove pyproject and tox bits, not supported by this package (bz 1881047)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Jerry James <loganjerry@gmail.com> - 0.3.0-1
- Version 0.3.0

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.2.12-1
- Version 0.2.12

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.11-2
- Rebuilt for Python 3.9

* Thu Apr 23 2020 Jerry James <loganjerry@gmail.com> - 0.2.11-1
- Version 0.2.11

* Thu Apr  2 2020 Jerry James <loganjerry@gmail.com> - 0.2.10-1
- Version 0.2.10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec  6 2019 Jerry James <loganjerry@gmail.com> - 0.2.6-2
- Ship the LICENSE file with the -doc subpackage too

* Thu Dec  5 2019 Jerry James <loganjerry@gmail.com> - 0.2.6-1
- Initial RPM
