%global pkg ddskk
%global pkgname Daredevil SKK
%global codename Neppu

Summary: Daredevil SKK - Simple Kana to Kanji conversion program for Emacs
Name: emacs-common-ddskk
Version: 17.1
Release: %{?autorelease}%{!?autorelease:1%{?dist}}
License: GPLv2+
URL: http://openlab.ring.gr.jp/skk/main.html
Source0: https://github.com/skk-dev/ddskk/archive/refs/tags/ddskk-%{version}_%{codename}.tar.gz
Source1: ddskk-init.el
BuildArch: noarch
BuildRequires: emacs
%if 0%{?fedora} < 36
BuildRequires: xemacs, apel-xemacs
%endif
BuildRequires: make
Requires(post): info
Requires(preun): info

%description
Daredevil SKK is a branch of SKK (Simple Kana to Kanji conversion program,
an input method of Japanese). It forked from the maintrunk, SKK version 10.56.
It consists of a simple core and many optional programs which provide extensive
features, however, our target is to more simplify core, and more expand its
optional features.

This package does not include dictionaries or a skkserver. Please install them
separately.

%package -n emacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under GNU Emacs
Requires:	emacs(bin) >= %{_emacs_version}
Requires:	emacs-common-%{pkg} = %{version}-%{release}
Provides:	ddskk = %{version}-%{release}
Obsoletes:	ddskk < %{version}-%{release}
Provides:	emacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	emacs-%{pkg}-el < %{version}-%{release}
%if 0%{?fedora} >= 36
Obsoletes:	xemacs-%{pkg} < 16.2-11
%endif

%description -n emacs-%{pkg}
This package contains the byte compiled elisp packages to run %{pkgname}
with GNU Emacs.


%if 0%{?fedora} < 36
%package -n xemacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under XEmacs
Requires:	xemacs(bin) >= %{_xemacs_version}
Requires:	apel-xemacs
Requires:	emacs-common-%{pkg} = %{version}-%{release}
Provides:	ddskk = %{version}-%{release}
Provides:	xemacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	xemacs-%{pkg}-el < %{version}-%{release}

%description -n xemacs-%{pkg}
This package contains the byte compiled elisp packages to use %{pkgname} with
XEmacs.
%endif


%prep
%autosetup -n %{pkg}-%{pkg}-%{version}_%{codename}

# We can't set SKK-MK-texinfo-coding-system in SKK-CFG since it is
# defined with defconst.

sed -ie "s!\(SKK-MK-texinfo-coding-system\) 'iso-2022-jp!\1 'utf-8!" SKK-MK

# We don't need information about other platforms
rm READMEs/README.MacOSX.ja
rm READMEs/README.w32.ja.org

# avoid buildroot in tutorial path
sed -ie "s!@TUT@!%{_datadir}/skk/SKK.tut!" skk-setup.el.in


%build


%install
# needed for make install-info
mkdir -p %{buildroot}%{_datadir}/info

cat >> SKK-CFG <<EOF
(setq PREFIX "%{buildroot}%{_prefix}")
(setq SKK_LISPDIR "%{buildroot}%{_emacs_sitelispdir}/ddskk")
EOF

make EMACS=emacs install

mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}

%if 0%{?fedora} < 36
make clean
cat >> SKK-CFG <<EOF
(setq SKK_PREFIX "ddskk")
(setq PACKAGEDIR "%{buildroot}%{_xemacs_sitepkgdir}")
EOF
make package
make install-package

mkdir -p %{buildroot}%{_xemacs_sitestartdir}
install -p -m 644 %SOURCE1 %{buildroot}%{_xemacs_sitestartdir}

rm %{buildroot}%{_xemacs_sitepkgdir}/info/skk.info*
%endif
rm -f %{buildroot}%{_infodir}/dir

%files
%doc ChangeLog READMEs
%{_datadir}/skk
%{_infodir}/*


%files -n emacs-%{pkg}
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/%{pkg}


%if 0%{?fedora} < 36
%files -n xemacs-%{pkg}
%{_xemacs_sitelispdir}/%{pkg}/*.elc
%{_xemacs_sitelispdir}/%{pkg}/*.el
%{_xemacs_sitestartdir}/*.el
%dir %{_xemacs_sitelispdir}/%{pkg}
%{_xemacs_sitepkgdir}/etc/%{pkg}/*
%dir %{_xemacs_sitepkgdir}/etc/%{pkg}
%endif


%changelog
%autochangelog
