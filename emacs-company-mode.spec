# TESTING NOTE: The tests require an Emacs running on a terminal, which is not
# possible in a mock build.  The maintainer should manually run "make test"
# prior to committing.

%global srcname company-mode

Name:           emacs-%{srcname}
Version:        0.9.13
Release:        4%{?dist}
Summary:        Modular in-buffer completion framework for Emacs

License:        GPL-3.0-or-later
URL:            https://company-mode.github.io/
Source0:        https://github.com/%{srcname}/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs

Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description
Company is a text completion framework for Emacs.  The name stands for
"complete anything".  It uses pluggable back-ends and front-ends to
retrieve and display completion candidates.  It comes with several
back-ends such as Elisp, Clang, Semantic, Eclim, Ropemacs, Ispell, CMake,
BBDB, Yasnippet, dabbrev, etags, gtags, files, keywords and a few others.

The CAPF back-end provides a bridge to the standard
completion-at-point-functions facility, and thus works with any major
mode that defines a proper completion function.

%prep
%autosetup -n %{srcname}-%{version}

%build
emacs -batch --no-init-file --no-site-file \
  --eval "(progn (setq generated-autoload-file \"$PWD/company-autoloads.el\" backup-inhibited t) (update-directory-autoloads \".\"))"
%_emacs_bytecompile *.el

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{srcname}
install -m 644 *.el{,c} %{buildroot}/%{_emacs_sitelispdir}/%{srcname}

mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv %{buildroot}/%{_emacs_sitelispdir}/%{srcname}/company-autoloads.el \
  %{buildroot}%{_emacs_sitestartdir}

%files
%doc NEWS.md README.md
%{_emacs_sitelispdir}/%{srcname}/
%{_emacs_sitestartdir}/company-autoloads.el

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 0.9.13-4
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 10 2021 Jerry James <loganjerry@gmail.com> - 0.9.13-1
- Initial RPM
