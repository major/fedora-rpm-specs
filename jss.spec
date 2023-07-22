################################################################################
Name:           jss
################################################################################

%global         product_id dogtag-jss

# Upstream version number:
%global         major_version 5
%global         minor_version 4
%global         update_version 2

# Downstream release number:
# - development/stabilization (unsupported): 0.<n> where n >= 1
# - GA/update (supported): <n> where n >= 1
%global         release_number 1

# Development phase:
# - development (unsupported): alpha<n> where n >= 1
# - stabilization (unsupported): beta<n> where n >= 1
# - GA/update (supported): <none>
#global         phase

%undefine       timestamp
%undefine       commit_id

Summary:        Java Security Services (JSS)
URL:            https://github.com/dogtagpki/jss
License:        MPL-1.1 or GPL-2.0-or-later or LGPL-2.1-or-later
Version:        5.4.2
Release:        %{release_number}%{?phase:.}%{?phase}%{?timestamp:.}%{?timestamp}%{?commit_id:.}%{?commit_id}%{?dist}.1

# To generate the source tarball:
# $ git clone https://github.com/dogtagpki/jss.git
# $ cd jss
# $ git tag v4.5.<z>
# $ git push origin v4.5.<z>
# Then go to https://github.com/dogtagpki/jss/releases and download the source
# tarball.
Source:         https://github.com/dogtagpki/jss/archive/v%{version}%{?phase:-}%{?phase}/jss-%{version}%{?phase:-}%{?phase}.tar.gz

# To create a patch for all changes since a version tag:
# $ git format-patch \
#     --stdout \
#     <version tag> \
#     > jss-VERSION-RELEASE.patch
# Patch: jss-VERSION-RELEASE.patch

%if 0%{?fedora} && 0%{?fedora} > 35
ExclusiveArch: %{java_arches}
%else
ExcludeArch: i686
%endif

################################################################################
# Java
################################################################################

%define java_devel java-17-openjdk-devel
%define java_headless java-17-openjdk-headless
%define java_home %{_jvmdir}/jre-17-openjdk

################################################################################
# Build Options
################################################################################

# By default the javadoc package will be built unless --without javadoc
# option is specified.

%bcond_without javadoc

# By default the build will not execute unit tests unless --with tests
# option is specified.

%bcond_with tests

################################################################################
# Build Dependencies
################################################################################

BuildRequires:  make
BuildRequires:  cmake >= 3.14
BuildRequires:  zip
BuildRequires:  unzip

BuildRequires:  gcc-c++
BuildRequires:  nss-devel >= 3.66
BuildRequires:  nss-tools >= 3.66

BuildRequires:  %{java_devel}
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-jdk14)
BuildRequires:  mvn(junit:junit)

%description
Java Security Services (JSS) is a java native interface which provides a bridge
for java-based applications to use native Network Security Services (NSS).
This only works with gcj. Other JREs require that JCE providers be signed.

################################################################################
%package -n %{product_id}
################################################################################

Summary:        Java Security Services (JSS)

Requires:       nss >= 3.66

Requires:       %{java_headless}
Requires:       mvn(org.apache.commons:commons-lang3)
Requires:       mvn(org.slf4j:slf4j-api)
Requires:       mvn(org.slf4j:slf4j-jdk14)

Obsoletes:      jss < %{version}-%{release}
Provides:       jss = %{version}-%{release}
Provides:       jss = %{major_version}.%{minor_version}
Provides:       %{product_id} = %{major_version}.%{minor_version}

Conflicts:      ldapjdk < 4.20
Conflicts:      idm-console-framework < 1.2
Conflicts:      tomcatjss < 7.6.0
Conflicts:      pki-base < 10.10.0

%description -n %{product_id}
Java Security Services (JSS) is a java native interface which provides a bridge
for java-based applications to use native Network Security Services (NSS).
This only works with gcj. Other JREs require that JCE providers be signed.

%if %{with javadoc}
################################################################################
%package -n %{product_id}-javadoc
################################################################################

Summary:        Java Security Services (JSS) Javadocs

Obsoletes:      jss-javadoc < %{version}-%{release}
Provides:       jss-javadoc = %{version}-%{release}
Provides:       jss-javadoc = %{major_version}.%{minor_version}
Provides:       %{product_id}-javadoc = %{major_version}.%{minor_version}

%description -n %{product_id}-javadoc
This package contains the API documentation for JSS.
%endif

################################################################################
%prep
################################################################################

%autosetup -n jss-%{version}%{?phase:-}%{?phase} -p 1

################################################################################
%build
################################################################################

# Set build flags for CMake
# (see /usr/lib/rpm/macros.d/macros.cmake)
%set_build_flags

export JAVA_HOME=%{java_home}

# Enable compiler optimizations
export BUILD_OPT=1

# Generate symbolic info for debuggers
CFLAGS="-g $RPM_OPT_FLAGS"
export CFLAGS

# Check if we're in FIPS mode
modutil -dbdir /etc/pki/nssdb -chkfips true | grep -q enabled && export FIPS_ENABLED=1

./build.sh \
    %{?_verbose:-v} \
    --work-dir=%{_vpath_builddir} \
    --prefix-dir=%{_prefix} \
    --include-dir=%{_includedir} \
    --lib-dir=%{_libdir} \
    --sysconf-dir=%{_sysconfdir} \
    --share-dir=%{_datadir} \
    --cmake=%{__cmake} \
    --java-home=%{java_home} \
    --jni-dir=%{_jnidir} \
    --version=%{version} \
    %{!?with_javadoc:--without-javadoc} \
    %{?with_tests:--with-tests} \
    dist

################################################################################
%install
################################################################################

./build.sh \
    %{?_verbose:-v} \
    --work-dir=%{_vpath_builddir} \
    --install-dir=%{buildroot} \
    install

################################################################################
%files -n %{product_id}
################################################################################

%defattr(-,root,root,-)
%doc jss.html
%license MPL-1.1.txt gpl.txt lgpl.txt symkey/LICENSE
%{_libdir}/*
%{_jnidir}/*

%if %{with javadoc}
################################################################################
%files -n %{product_id}-javadoc
################################################################################

%defattr(-,root,root,-)
%{_javadocdir}/jss/
%endif

################################################################################
%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Packit <hello@packit.dev> - 5.4.2-1
- Updating version to v5.4.2 (Chris Kelley)
- Upstream spec file changes to reduce diffs (Chris Kelley)
- Introduce Packit configuration for jss (Chris Kelley)

* Tue Feb 07 2023 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.3.0-2
- Update version number in JSSConfig.cmake

* Tue Feb 07 2023 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.3.0-1
- Rebase to JSS 5.3.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.2.0-1
- Rebase to JSS 5.2.0

* Wed Apr 27 2022 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.2.0-0.3.beta2
- Rebase to JSS 5.2.0-beta2
- Rename packages to dogtag-jss

* Mon Apr 11 2022 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.2.0-0.2.beta1
- Rebase to JSS 5.2.0-beta1

* Mon Feb 14 2022 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.1.0-1
- Rebase to JSS 5.1.0

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 5.1.0-0.3.alpha2
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-0.2.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.1.0-0.1.alpha2
- Rebase to JSS 5.1.0-alpha2

* Thu Sep 30 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.0.0-1
- Rebase to JSS 5.0.0

* Wed Sep 29 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.0.0-0.5.beta1
- Drop BuildRequires and Requires on glassfish-jaxb-api

* Fri Sep 03 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.0.0-0.4.beta1
- Rebase to JSS 5.0.0-beta1

* Thu Aug 12 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.0.0-0.3.alpha2
- Rebase to JSS 5.0.0-alpha2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.2.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> - 5.0.0-0.1.alpha1
- Rebase to JSS 5.0.0-alpha1
