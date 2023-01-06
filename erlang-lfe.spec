%global realname lfe
%global upstream rvirding

# Set this to true when starting a rebuild of the whole erlang stack. There's a
# cyclical dependency between erlang-erts, erlang-lfe, and erlang-rebar so this
# package (erlang-lfe) needs to get built first in bootstrap mode.
%global need_bootstrap 0


%if 0%{?need_bootstrap}
%global _erllibdir %{_libdir}/erlang/lib
%global debug_package %{nil}
%endif


Name:		erlang-%{realname}
Version:	2.1.1
Release:	1%{?dist}
Summary:	Lisp Flavoured Erlang
License:	BSD
URL:		https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
%if 0%{?need_bootstrap}
BuildRequires:	erlang-erts
BuildRequires:	erlang-rpm-macros
%else
BuildRequires:	erlang-rebar
%endif
BuildRequires:	pkgconfig
BuildRequires:	emacs
BuildRequires:	emacs-el
BuildRequires:	gcc
Requires:	emacs-filesystem
Obsoletes:	emacs-erlang-lfe
Obsoletes:	emacs-erlang-lfe-el
%{?__erlang_drv_version:Requires: %{__erlang_drv_version}}


%description
Lisp Flavoured Erlang, is a lisp syntax front-end to the Erlang
compiler. Code produced with it is compatible with "normal" Erlang
code. An LFE evaluator and shell is also included.

%prep
%autosetup -p 1 -n %{realname}-%{version}


%build
%if 0%{?need_bootstrap}
mkdir -p ./ebin/
/usr/bin/erlc -o ./ebin/ src/*.erl
%else
mkdir -p ./ebin/
%{erlang_compile}
%endif
emacs -L emacs/ -batch -f batch-byte-compile emacs/inferior-lfe.el emacs/lfe-mode.el emacs/lfe-indent.el


%install
install -m 0755 -d %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/{bin,ebin,priv}
install -p -m 0755 -D ebin/* %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m 0755 -D bin/*  %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/bin/
%if 0%{?need_bootstrap}
echo "we are going to install only bare minimum of LFE - just for rebar bootstrapping"
%else
install -p -m 0755 priv/%{realname}_drv.so %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/priv/
%endif
install -m 0755 -d %{buildroot}/%{_bindir}
ln -s %{_libdir}/erlang/lib/%{realname}-%{version}/bin/{lfe,lfec,lfescript} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_emacs_sitelispdir}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 emacs/inferior-lfe.el %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/inferior-lfe.elc %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-mode.el %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-mode.elc %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-indent.el %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-indent.elc %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-start.el %{buildroot}%{_emacs_sitestartdir}


%check
%if 0%{?need_bootstrap}
echo "No tests during bootstrapping"
%else
#%%{erlang_test}
%endif


%files
%license LICENSE
%doc README.md doc/ examples/
%{_bindir}/lfe
%{_bindir}/lfec
%{_bindir}/lfescript
%{erlang_appdir}/
%{_emacs_sitelispdir}/inferior-lfe.el
%{_emacs_sitelispdir}/inferior-lfe.elc
%{_emacs_sitelispdir}/lfe-indent.el
%{_emacs_sitelispdir}/lfe-indent.elc
%{_emacs_sitelispdir}/lfe-mode.el
%{_emacs_sitelispdir}/lfe-mode.elc
%{_emacs_sitestartdir}/lfe-start.el


%changelog
* Wed Jan  4 2023 Peter Lemenkov <lemenkov@gmail.com> - 2.1.1-1
- LFE ver. 2.1.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Peter Lemenkov <lemenkov@gmail.com> - 2.0.1-1
- LFE ver. 2.0.1

* Tue Jul 27 2021 Peter Lemenkov <lemenkov@gmail.com> - 2.0.1-0.1
- Bootstrap ver. 2.0.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.3-1
- Ver. 1.3

* Tue Jun 20 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.3-0
- Bootstrap ver. 1.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1
- Ver. 1.2.1
- Disable tests for now

* Wed Nov 23 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-0
- Bootstrap ver. 1.2.1

* Thu Oct 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0

* Wed Jun  8 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-2
- No longer providing separate emacs-subpackages

* Sat Apr 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-1
- Ver. 1.0.2

* Mon Apr  4 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-2
- Ver. 1.0.1

* Mon Apr  4 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-1
- Ver. 1.0.1 (bootstrap)

* Wed Mar 30 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.10.1-3
- Rebuild with Erlang 18.3

* Wed Mar 30 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.10.1-2.1
- Bootstrap (build w/o rebar) against Erlang 18.3

* Tue Mar  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.10.1-2
- Install CLI tools as well

* Tue Mar  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.10.1-1
- Ver. 0.10.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.9.0-2
- Disable debuginfo

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.9.0-1
- Ver. 0.9.0
- Drop support for EL5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.6.2-1
- Ver. 0.6.2 (Backwards API/ABI compatible)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-5
- Make building of emacs sub-packages conditional (and disable on EL-5)

* Sun Nov 14 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-4
- Remove duplicated emacs files from docs

* Sun Oct 31 2010 Tim Niemueller <tim@niemueller.de> - 0.6.1-3
- Added Emacs sub-package
- Fix inconsitent macro usage

* Fri Oct 15 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-2
- Provide (x)emacs subpackages

* Fri Oct  1 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-1
- Initial build
