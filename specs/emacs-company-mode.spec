# TESTING NOTE: The tests require an Emacs running on a terminal, which is not
# possible in a mock build.  The maintainer should manually run "make test"
# prior to committing.

%global srcname company-mode
%global giturl  https://github.com/company-mode/company-mode

Name:           emacs-%{srcname}
Version:        1.0.2
Release:        %autorelease
Summary:        Modular in-buffer completion framework for Emacs

License:        GPL-3.0-or-later
URL:            https://company-mode.github.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/%{srcname}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

BuildRequires:  emacs-nw

Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description
Company is a text completion framework for Emacs.  The name stands for
"complete anything".  It uses pluggable back-ends and front-ends to retrieve
and display completion candidates.  It comes with several back-ends such as
Elisp, Clang, Semantic, Eclim, Ropemacs, Ispell, CMake, BBDB, Yasnippet,
dabbrev, etags, gtags, files, keywords and a few others.

The CAPF back-end provides a bridge to the standard
completion-at-point-functions facility, and thus works with any major mode
that defines a proper completion function.

%prep
%autosetup -n %{srcname}-%{version}

%build
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/company-loaddefs.el\"))"
%_emacs_bytecompile *.el

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{srcname}
install -p -m 644 *.el{,c} %{buildroot}/%{_emacs_sitelispdir}/%{srcname}

mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv %{buildroot}/%{_emacs_sitelispdir}/%{srcname}/company-loaddefs.el \
  %{buildroot}%{_emacs_sitestartdir}

%files
%doc NEWS.md README.md
%{_emacs_sitelispdir}/%{srcname}/
%{_emacs_sitestartdir}/company-loaddefs.el

%changelog
%autochangelog
