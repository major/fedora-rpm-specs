Name:           lmdb
Version:        0.9.30
Release:        %autorelease
Summary:        Memory-mapped key-value database
License:        OpenLDAP
URL:            https://www.symas.com/lmdb

# Main source is retrieved from OpenLDAP GitLab
%global forgeurl    https://git.openldap.org/openldap/openldap
%global tag         LMDB_%{version}
%global archivename openldap-%{tag}
%global archiveext  tar.gz
%global archiveurl  %{forgeurl}/-/archive/%{tag}/%{archivename}.%{archiveext}
%forgemeta

Source:         %{forgesource}
Source:         lmdb.pc.in
# Patch description in the corresponding file
Patch:          lmdb-make.patch
Patch:          lmdb-s390-check.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  doxygen

%description
LMDB is an ultra-fast, ultra-compact key-value embedded data
store developed by Symas for the OpenLDAP Project. By using memory-mapped files,
it provides the read performance of a pure in-memory database while still
offering the persistence of standard disk-based databases, and is only limited
to the size of the virtual address space.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs
The %{name}-libs package contains shared libraries necessary for running
applications that use %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains automatically generated documentation for %{name}.


%prep
# forgeautosetup does not pass the -n argument
%autosetup -n %{archivename} -p1

# The files themselves are in several subdirectories and need to be prefixed wit this.
%global archive_path libraries/lib%{name}

%build
pushd %{archive_path}
%set_build_flags
%make_build XCFLAGS="%{build_cflags}"
# Build doxygen documentation
doxygen
# remove unpackaged files
rm -f Doxyfile
rm -rf man # Doxygen generated manpages
popd

%install
pushd %{archive_path}
# make install expects existing directory tree
mkdir -m 0755 -p %{buildroot}{%{_bindir},%{_includedir}}
mkdir -m 0755 -p %{buildroot}{%{_libdir}/pkgconfig,%{_mandir}/man1}
%make_install prefix=%{_prefix} libdir=%{_libdir} mandir=%{_mandir}
popd

# Install pkgconfig file
sed -e 's:@PREFIX@:%{_prefix}:g' \
    -e 's:@EXEC_PREFIX@:%{_exec_prefix}:g' \
    -e 's:@LIBDIR@:%{_libdir}:g' \
    -e 's:@INCLUDEDIR@:%{_includedir}:g' \
    -e 's:@PACKAGE_VERSION@:%{version}:g' \
    %{SOURCE1} >lmdb.pc
install -Dpm 0644 -t %{buildroot}%{_libdir}/pkgconfig lmdb.pc

%check
%if 0%{?rhel} == 6 && "%{_arch}" == "ppc64"
  # rhel6 ppc64: skip unit tests
  exit 0
%endif

pushd %{archive_path}
rm -rf testdb
LD_LIBRARY_PATH=$PWD make test
popd

%ldconfig_scriptlets libs


%files
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%doc %{archive_path}/COPYRIGHT
%doc %{archive_path}/CHANGES
%license %{archive_path}/LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{archive_path}/html
%doc %{archive_path}/COPYRIGHT
%doc %{archive_path}/CHANGES
%license %{archive_path}/LICENSE


%changelog
%autochangelog
