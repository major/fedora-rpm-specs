%global pkg slime

Name:            emacs-%{pkg}
Epoch:           2
Version:         2.32
Release:         %autorelease
Summary:         The superior lisp interaction mode for emacs        

#Public domain: Mentioned in README file
#LLGPL: Mentioned in swank-ccl.lisp
#GPLv2+: slime.el,slime-autoloads.el
#GPLv3+: Many files in contrib are GPLv3+
License:         LicenseRef-Fedora-Public-Domain AND GPL-3.0-or-later AND GPL-2.0-or-later AND LLGPL
URL:             http://common-lisp.net/project/slime/
Source0:         https://github.com/slime/slime/archive/v%{version}.tar.gz#/%{pkg}-%{version}.tar.gz

BuildRequires:   common-lisp-controller
BuildRequires:   emacs
BuildRequires:   make
BuildRequires:   texinfo

# for testing
BuildRequires:   sbcl

Requires:        emacs(bin) >= %{_emacs_version} common-lisp-controller

Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

Provides:        %{name}-el = %{epoch}:%{version}-%{release}
Obsoletes:       %{name}-el < 1:2.19-5

BuildArch:      noarch
# taken from sbcl.spec since we use it for testing
ExclusiveArch:  %{arm} %{ix86} x86_64 ppc sparcv9 aarch64

%description
SLIME is a Emacs mode for common Lisp development.

%prep
%autosetup -n %{pkg}-%{version} -p1

%build
#{_emacs_bytecompile} *.el
make
cd doc/
make slime.info

%install
install -pm 755 -d %{buildroot}%{_emacs_sitestartdir}
install -pm 644 *.el  %{buildroot}%{_emacs_sitestartdir}

install -pm 755 -d %{buildroot}%{_infodir}
install -pm 644 doc/%{pkg}.info %{buildroot}%{_infodir}/

install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/contrib
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/lib
install -pm 644 *.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -pm 644 lib/*.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/lib/


install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime/lib
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime/swank
install -pm 644 *.lisp %{buildroot}%{_datadir}/common-lisp/source/slime
install -pm 644 contrib/*.lisp %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 644 contrib/*.el %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 644 contrib/README.md %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 644 lib/*.el %{buildroot}%{_datadir}/common-lisp/source/slime/lib
install -pm 644 swank/*.lisp %{buildroot}%{_datadir}/common-lisp/source/slime/swank
install -pm 644 *.asd %{buildroot}%{_datadir}/common-lisp/source/slime

mv contrib/README.md contrib/contrib-README.md

%check
make check

%post
/usr/sbin/register-common-lisp-source swank

%preun
/usr/sbin/unregister-common-lisp-source swank 

%files
%doc NEWS PROBLEMS README.md doc/slime-small.pdf doc/slime-refcard.pdf contrib/contrib-README.md
%doc CONTRIBUTING.md

%dir %{_emacs_sitestartdir}
%{_emacs_sitestartdir}/*.el

%dir %{_emacs_sitelispdir}/%{pkg}
%dir %{_emacs_sitelispdir}/%{pkg}/contrib
%dir %{_emacs_sitelispdir}/%{pkg}/lib
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitelispdir}/%{pkg}/lib/*.el
%{_emacs_sitelispdir}/%{pkg}/lib/*.elc

%dir %{_datadir}/common-lisp/source/slime
%dir %{_datadir}/common-lisp/source/slime/contrib
%dir %{_datadir}/common-lisp/source/slime/lib
%{_datadir}/common-lisp/source/slime/*.lisp
%{_datadir}/common-lisp/source/slime/contrib/*.lisp
%{_datadir}/common-lisp/source/slime/contrib/*.el
%{_datadir}/common-lisp/source/slime/lib/*.el
%{_datadir}/common-lisp/source/slime/swank/*.lisp
%{_datadir}/common-lisp/source/slime/contrib/README.md
%{_datadir}/common-lisp/source/slime/*.asd
%{_infodir}/%{pkg}.info.*

%changelog
%autochangelog
