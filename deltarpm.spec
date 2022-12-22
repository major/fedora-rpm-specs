Name:           deltarpm
Summary:        Create deltas between rpms
Version:        3.6.3
Release:        %autorelease
License:        BSD
URL:            https://github.com/rpm-software-management/deltarpm
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          https://github.com/rpm-software-management/deltarpm/pull/17.patch#./Don_t-use-the-deprecated-Python-distutils-module-in-the-Makefile.patch
BuildRequires:  gcc
BuildRequires:  bzip2-devel
BuildRequires:  libzstd-devel
BuildRequires:  perl-generators
BuildRequires:  xz-devel
BuildRequires:  rpm-devel
BuildRequires:  popt-devel
BuildRequires:  zlib-devel

%description
A deltarpm contains the difference between an old
and a new version of a rpm, which makes it possible
to recreate the new rpm from the deltarpm and the old
one. You don't have to have a copy of the old rpm,
deltarpms can also work with installed rpms.

%package -n drpmsync
Summary:        Sync a file tree with deltarpms
Requires:       %{name}%{_isa} = %{version}-%{release}

%description -n drpmsync
This package contains a tool to sync a file tree with
deltarpms.

%package -n deltaiso
Summary:        Create deltas between isos containing rpms
Requires:       %{name}%{_isa} = %{version}-%{release}

%description -n deltaiso
This package contains tools for creating and using deltasisos,
a difference between an old and a new iso containing rpms.

%package -n python3-%{name}
Summary:        Python bindings for deltarpm
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires: make
Requires:       %{name}%{_isa} = %{version}-%{release}

%description -n python3-%{name}
This package contains python bindings for deltarpm.

Python 3 version.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build CFLAGS="${CFLAGS} -DWITH_ZSTD=1" \
    bindir=%{_bindir} libdir=%{_libdir} mandir=%{_mandir} prefix=%{_prefix} \
    zlibbundled='' zlibldflags='-lz' zlibcppflags=''

%make_build CFLAGS="${CFLAGS} -DWITH_ZSTD=1" \
    bindir=%{_bindir} libdir=%{_libdir} mandir=%{_mandir} prefix=%{_prefix} \
    zlibbundled='' zlibldflags='-lz' zlibcppflags='' \
    python

%install
# cannot use %%make_install here, as then prefix is not passed into the Makefile
%make_build pylibprefix=%{buildroot} mandir=%{buildroot}%{_mandir} prefix=%{buildroot}%{_prefix} install

%files
%license LICENSE.BSD
%doc README NEWS
%{_bindir}/applydeltarpm
%{_mandir}/man8/applydeltarpm.8*
%{_bindir}/combinedeltarpm
%{_mandir}/man8/combinedeltarpm.8*
%{_bindir}/makedeltarpm
%{_mandir}/man8/makedeltarpm.8*
%{_bindir}/rpmdumpheader

%files -n deltaiso
%{_bindir}/applydeltaiso
%{_mandir}/man8/applydeltaiso.8*
%{_bindir}/fragiso
%{_mandir}/man8/fragiso.8*
%{_bindir}/makedeltaiso
%{_mandir}/man8/makedeltaiso.8*

%files -n drpmsync
%{_bindir}/drpmsync
%{_mandir}/man8/drpmsync.8*

%files -n python3-%{name}
%{python3_sitearch}/%{name}.py
%{python3_sitearch}/_%{name}module.so
%{python3_sitearch}/__pycache__/%{name}.*

%changelog
%autochangelog
