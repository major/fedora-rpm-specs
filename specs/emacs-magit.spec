%define pkg magit
%define pkgname Magit

Name:           emacs-%{pkg}
Version:        3.3.0
Release:        7%{?dist}
Summary:        Emacs interface to the most common Git operations
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://magit.vc

Source0:        https://github.com/magit/magit/releases/download/v%{version}/magit-%{version}.tar.gz
Source1:        magit-init.el

BuildArch:      noarch
BuildRequires:  emacs emacs-async emacs-dash
BuildRequires:  emacs-with-editor make texinfo git-core
BuildRequires:  emacs-transient > 0.2.0-1
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-async emacs-dash emacs-transient emacs-with-editor
Requires:       git-core
Obsoletes:      emacs-%{pkg}-el < %{version}-%{release}
Provides:       emacs-%{pkg}-el = %{version}-%{release}

%description
%{pkgname} is an add-on package for GNU Emacs. It is an interface to
the Git source-code management system that aims to make the most
common operations convenient.

%prep
%autosetup -n %{pkg}-%{version}

%global MAKE_PARMS VERSION="%{version}-%{release}" LOAD_PATH="-L %{_emacs_sitelispdir}/dash -L %{_emacs_sitelispdir}/transient -L %{_emacs_sitelispdir}/with-editor -L $(pwd)/lisp"

%build
make BUILD_MAGIT_LIBGIT=false \
    %{MAKE_PARMS} \
    versionlib all

%check
# Some tests depend on a full git repository, so add a simple test here.
emacs --batch -L lisp -l %{pkg} -f %{pkg}-version 2>&1 \
    | grep "%{pkgname} %{version}"

%install
make install \
    %{MAKE_PARMS} \
    DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} BUILD_MAGIT_LIBGIT=false

# clean up after magit's installer's assumptions
rm ${RPM_BUILD_ROOT}/%{_docdir}/%{pkg}/AUTHORS.md

mkdir -p %{buildroot}%{_emacs_sitestartdir}/
cp -p %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/

%files
%license LICENSE
%doc README.md
%{_emacs_sitelispdir}/%{pkg}
%{_emacs_sitestartdir}/magit-init.el
%{_infodir}/%{pkg}*.info.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.0-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Jens Petersen <petersen@redhat.com> - 3.3.0-1
- update to 3.3.0 (#1964366)
- restore magit-init.el to autoload magit-status

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.90.1-6.20201015git084498406
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.90.1-5.20201015git084498406
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.90.1-4.20201015git084498406
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.90.1-3.20201015git084498406
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 02 2021 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 2.90.1-2.20201015.git084498406
- Update to commit ID 08449840608ab20c0361caf2174628fd188dba5a.
- Fix the absence of magit-git.el.

* Thu Jan 28 2021 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 2.90.1-1.20200909.gitd58d520e5
- Update to commit ID d58d520e586b70172601ee2814a5e053ca74d1d9.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 2.4.1-1
- Modernize the SPEC file.
- Add a simple test.
- Install the license.

* Thu Sep 10 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 2.4.1-0
- Update to magit 2.4.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.2-10
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Jens Petersen <petersen@redhat.com> - 1.2.2-5
- drop the el subpackage (#1234540)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan  4 2015 Jens Petersen <petersen@redhat.com> - 1.2.2-1
- update to 1.2.2 which works with emacs-24.4 (#1172690)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Tom Moertel <tom@moertel.com> - 1.2.0-1
- Update to upstream version 1.2.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 25 2012 Tom Moertel <tom@moertel.com> - 1.1.1-1
- Update to upstream 1.1.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 13 2011 Tom Moertel <tom@moertel.com> - 1.0.0-1
- Updated to upstream 1.0.0

* Wed Aug  4 2010 Tom Moertel <tom@moertel.com> - 0.8.2-1
- Updated to upstream 0.8.2

* Wed Aug 26 2009 Tom Moertel <tom@moertel.com> - 0.7-6
- Updated for Magit 0.7 final release (note: upstream removed FDL from tarball)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5.20090122git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4.20090122git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009  <tom@moertel.com> - 0.7-3.20090122git
- Added missing build dependency: texinfo

* Tue Jan 27 2009  <tom@moertel.com> - 0.7-2.20090122git
- Made fixes per Fedora packaging review (thanks Jerry James)

* Fri Jan 23 2009  <tom@moertel.com> - 0.7-1.20090122git
- Initial packaging.
