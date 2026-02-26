%global debug_package %{nil}

%global macros_dir %{_rpmconfigdir}/macros.d

Name:           ghc-rpm-macros
Version:        2.11
Release:        %autorelease
Summary:        RPM macros for building Haskell packages for GHC

License:        GPL-3.0-or-later
# Currently source is only in pkg git but tarballs could be made if it helps
URL:            https://src.fedoraproject.org/rpms/ghc-rpm-macros/
Source0:        macros.ghc
Source1:        COPYING
Source2:        AUTHORS
Source3:        ghc-deps.sh
Source4:        cabal-tweak-dep-ver
Source5:        cabal-tweak-flag
Source6:        macros.ghc-extra
Source7:        ghc.attr
Source8:        ghc-pkg-wrapper
Source9:        macros.ghc-os
Source10:       Setup.hs
Source11:       cabal-tweak-drop-dep
Source12:       cabal-tweak-remove-upperbound
Source13:       ghc-info.sh
Source14:       macros.ghc-srpm-quick
Requires:       redhat-rpm-config
# ghc_version needs ghc-compiler or ghcX.Y-compiler-default
Requires:       chrpath
BuildArch:      noarch

%description
A set of macros for building GHC packages following the Haskell Guidelines
of the Fedora Haskell SIG.


%package extra
Summary:        Extra RPM macros for building Haskell library subpackages
Requires:       %{name} = %{version}-%{release}

%description extra
Extra macros used for subpackaging of Haskell libraries,
for example in ghc and haskell-platform.


%package quick
Summary:        Disables building of ghc prof and doc subpackages
Requires:       %{name} = %{version}-%{release}
# added during F40 cycle
Obsoletes:      %{name}-no-prof < %{version}-%{release}
Provides:       %{name}-no-prof = %{version}-%{release}

%description quick
Overrides ghc-srpm-macros to disable building ghc prof and doc subpackages
locally.

This should not be used in official Fedora builds.


%if %{defined el9} || %{defined el8}
%package -n ghc-filesystem
Summary:        Shared directories for Haskell documentation

%description -n ghc-filesystem
This package provides some common directories used for
Haskell libraries documentation.
%endif

%global ghc_obsoletes_binlib()\
Obsoletes: %1 < %2, %1-common < %2\
%ghc_obsoletes_lib %1 %2

%global ghc_obsoletes_lib()\
Obsoletes: ghc-%1 < %2, ghc-%1-devel < %2, ghc-%1-doc < %2, ghc-%1-prof < %2

%global ghc_obsoletes_lib_eq()\
Obsoletes: ghc-%1 = %2, ghc-%1-devel = %2, ghc-%1-doc = %2, ghc-%1-prof = %2

# ideally packages should be obsoleted by some relevant package
# this is a last resort when there is no such appropriate package
%package -n ghc-obsoletes
Summary:        Dummy package to obsolete deprecated Haskell packages
%if 0%{?fedora} >= 36
%ghc_obsoletes_lib regex-applicative-text 0.1.0.1-16
%endif
%if 0%{?fedora} >= 38
%ghc_obsoletes_lib bytestring-show 0.3.5.7
%ghc_obsoletes_lib djinn-ghc 0.1
%ghc_obsoletes_lib ghc-mtl 1.2.2
%ghc_obsoletes_lib ghc-syb-utils 0.3.1
%ghc_obsoletes_lib cabal-helper 1.2
%ghc_obsoletes_lib cabal-plan 0.8
%ghc_obsoletes_lib optics-core 0.4
%ghc_obsoletes_lib semialign 1.2
%ghc_obsoletes_lib topograph 1.0.0.2
%ghc_obsoletes_lib indexed-profunctors 0.1.1-18
%ghc_obsoletes_lib regex-compat-tdfa 0.95.1.4-38
%endif
%if 0%{?fedora} >= 39
%ghc_obsoletes_lib geniplate-mirror 0.7.9-39
%ghc_obsoletes_lib data-array-byte 0.1.0.1-3
%endif
%if 0%{?fedora} >= 41
%ghc_obsoletes_lib ConfigFile 1.1.4.0
%ghc_obsoletes_lib MonadCatchIO-mtl 0.3.1.1
%ghc_obsoletes_lib MonadCatchIO-transformers 0.3.1.4
%ghc_obsoletes_lib connection 0.3.1.0
%ghc_obsoletes_lib cprng-aes 0.6.1.0
%ghc_obsoletes_lib crypto-random 0.0.9.0
%ghc_obsoletes_lib cryptohash 0.11.9.0
%ghc_obsoletes_lib fedora-dists 2.1.1.0
%ghc_obsoletes_lib foldable1-classes-compat 0.1.0
%ghc_obsoletes_lib highlighting-kate 0.6.4.0
%ghc_obsoletes_lib libxml-sax 0.7.5.0
%ghc_obsoletes_lib monad-journal 0.8.1.0
%ghc_obsoletes_lib pdc 0.1.1.0
%ghc_obsoletes_lib regexpr 0.5.4.0
%ghc_obsoletes_lib x509 1.7.7.0
%ghc_obsoletes_lib x509-store 1.6.9.0
%ghc_obsoletes_lib x509-system 1.6.7.0
%ghc_obsoletes_lib x509-validation 1.6.12.0
%endif
%if 0%{?fedora} >= 43
%ghc_obsoletes_lib aeson-compat 0.3.11
%ghc_obsoletes_lib fclabels 2.0.5.2
%ghc_obsoletes_lib system-fileio 0.3.16.7
%ghc_obsoletes_lib libiserv 9.8
%endif
%if 0%{?fedora} >= 44
%ghc_obsoletes_lib breakpoint 0.1.5
%ghc_obsoletes_lib bytestring-nums 0.3.6.0
%ghc_obsoletes_lib data-default-instances-containers 0.1.0.4
%ghc_obsoletes_lib data-default-instances-dlist 0.0.1.3
%ghc_obsoletes_lib data-default-instances-old-locale 0.0.1.3
%ghc_obsoletes_lib_eq deepseq 0.5.1
%ghc_obsoletes_lib deferred-folds 0.9.18.8
%ghc_obsoletes_lib isomorphism-class 0.3.1
%ghc_obsoletes_lib lawful-conversions 0.1.7
%ghc_obsoletes_lib markdown-unlit 0.6.0.1
%ghc_obsoletes_lib mintty 0.1.4.0
%ghc_obsoletes_lib ormolu 0.7.7
%ghc_obsoletes_lib pager 0.1.1.1
%ghc_obsoletes_lib quickcheck-instances 0.3.33
%ghc_obsoletes_lib text-builder 0.6.8
%ghc_obsoletes_lib text-builder-dev 0.3.10
%ghc_obsoletes_lib th-env 0.1.1.0
%ghc_obsoletes_lib with-location 0.1.0.0
%endif

%description -n ghc-obsoletes
Meta package for obsoleting deprecated Haskell packages.

This package can safely be removed.


%prep
%setup -c -T
cp %{SOURCE1} %{SOURCE2} .


%build
echo no build stage


%install
install -p -D -m 0644 %{SOURCE0} %{buildroot}%{macros_dir}/macros.ghc
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{macros_dir}/macros.ghc-extra
install -p -D -m 0644 %{SOURCE9} %{buildroot}%{macros_dir}/macros.ghc-os
install -p -D -m 0644 %{SOURCE14} %{buildroot}%{macros_dir}/macros.ghc-srpm-quick

%if %{defined el9} || %{defined el8}
echo -e "\n%%_ghcdynlibdir %%{_libdir}" >> %{buildroot}%{macros_dir}/macros.ghc-os
%endif

install -p -D -m 0755 %{SOURCE3} %{buildroot}%{_prefix}/lib/rpm/ghc-deps.sh
install -p -D -m 0755 %{SOURCE13} %{buildroot}%{_prefix}/lib/rpm/ghc-info.sh

install -p -D -m 0644 %{SOURCE7} %{buildroot}%{_prefix}/lib/rpm/fileattrs/ghc.attr

install -p -D -m 0644 %{SOURCE10} %{buildroot}%{_datadir}/%{name}/Setup.hs

install -p -D -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/cabal-tweak-dep-ver
install -p -D -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/cabal-tweak-flag
install -p -D -m 0755 %{SOURCE11} %{buildroot}%{_bindir}/cabal-tweak-drop-dep
install -p -D -m 0755 %{SOURCE12} %{buildroot}%{_bindir}/cabal-tweak-remove-upperbound
install -p -D -m 0755 %{SOURCE8} %{buildroot}%{_prefix}/lib/rpm/ghc-pkg-wrapper

%if %{defined el9} || %{defined el8}
mkdir -p %{buildroot}%{_docdir}/ghc/html/libraries
%endif


%files
%license COPYING
%doc AUTHORS
%{macros_dir}/macros.ghc
%{macros_dir}/macros.ghc-os
%{_prefix}/lib/rpm/fileattrs/ghc.attr
%{_prefix}/lib/rpm/ghc-deps.sh
%{_prefix}/lib/rpm/ghc-info.sh
%{_prefix}/lib/rpm/ghc-pkg-wrapper
%{_bindir}/cabal-tweak-dep-ver
%{_bindir}/cabal-tweak-drop-dep
%{_bindir}/cabal-tweak-flag
%{_bindir}/cabal-tweak-remove-upperbound
%{_datadir}/%{name}/Setup.hs


%files extra
%{macros_dir}/macros.ghc-extra


%files quick
%{macros_dir}/macros.ghc-srpm-quick


%if %{defined el9} || %{defined el8}
%files -n ghc-filesystem
%dir %{_docdir}/ghc
# %%{ghc_html_dir}
%dir %{_docdir}/ghc/html
# %%{ghc_html_libraries_dir}
%dir %{_docdir}/ghc/html/libraries
%endif


%if %{defined fedora}
%files -n ghc-obsoletes
%endif


%changelog
%autochangelog
