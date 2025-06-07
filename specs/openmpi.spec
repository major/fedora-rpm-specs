# Optional name suffix to use...we leave it off when compiling with gcc, but
# for other compiled versions to install side by side, it will need a
# suffix in order to keep the names from conflicting.
#global _cc_name_suffix -gcc

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
%bcond_with python2
%else
%bcond_without python2
%endif

%ifarch aarch64 ppc64le x86_64
%bcond_without ucx
%else
%bcond_with ucx
%endif

# ARM 32-bit is not supported by rdma
# https://bugzilla.redhat.com/show_bug.cgi?id=1780584
%ifarch %{arm}
%bcond_with rdma
%else
%bcond_without rdma
%endif

# No more Java on i686
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

%if %{defined rhel}
%bcond_with orangefs
%bcond_with sphinx
%else
%bcond_without orangefs
%bcond_without sphinx
%endif

%ifarch x86_64
%if 0%{?rhel} >= 10
%bcond_with psm2
%else
%bcond_without psm2
%endif
%else
%bcond_with psm2
%endif

# Some RCs require unreleased pmix version - at least let us test builds
%bcond_without pmix

# Run autogen - needed for some patches
%bcond autogen 0

Name:           openmpi%{?_cc_name_suffix}
Version:        5.0.8
Release:        %autorelease
Summary:        Open Message Passing Interface
# Automatically converted from old format: BSD and MIT and Romio - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Romio
URL:            http://www.open-mpi.org/
ExcludeArch:    %{ix86}

# We can't use %%{name} here because of _cc_name_suffix
Source0:        https://www.open-mpi.org/software/ompi/v5.0/downloads/openmpi-%{version}.tar.bz2
Source1:        openmpi.module.in
Source2:        openmpi.pth.py2
Source3:        openmpi.pth.py3
Source4:        macros.openmpi

Patch0:         https://github.com/open-mpi/ompi/pull/13281.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
%if %{with autogen}
BuildRequires:  libtool
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Find)
%endif
%ifarch %{valgrind_arches}
BuildRequires:  valgrind-devel
%endif
%if %{with rdma}
BuildRequires:  opensm-devel > 3.3.0
BuildRequires:  rdma-core-devel
%endif
# Doesn't compile:
# vt_dyn.cc:958:28: error: 'class BPatch_basicBlockLoop' has no member named 'getLoopHead'
#                      loop->getLoopHead()->getStartAddress(), loop_stmts );
#BuildRequires:  dyninst-devel
BuildRequires:  hwloc-devel
# So configure can find lstopo
BuildRequires:  hwloc-gui
%if %{with java}
BuildRequires:  java-devel
%else
Obsoletes:      %{name}-java < %{version}-%{release}
Obsoletes:      %{name}-java-devel < %{version}-%{release}
%endif
# Old libevent causes issues
%if !0%{?el7}
BuildRequires:  libevent-devel
%endif
BuildRequires:  libfabric-devel
%ifnarch s390x
BuildRequires:  papi-devel
%endif
%if %{with orangefs}
BuildRequires:  orangefs-devel
%endif
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
%if %{with pmix}
BuildRequires:  pmix-devel >= 4.2.7
%endif
# For configure to find /usr/bin/prte
BuildRequires:  prrte
BuildRequires:  prrte-devel
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with psm2}
BuildRequires:  libpsm2-devel
%endif
%if %{with ucx}
BuildRequires:  ucx-devel
%endif
BuildRequires:  zlib-devel
%if !0%{?el7}
BuildRequires:  rpm-mpi-hooks
%endif
%if %{with sphinx}
# For docs
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  python3-recommonmark
BuildRequires:  python3-sphinx_rtd_theme
%endif

Provides:       mpi
%if 0%{?rhel} == 7
# Need this for /etc/profile.d/modules.sh
Requires:       environment-modules
%endif
Requires:       environment(modules)
Requires:       prrte
# openmpi currently requires ssh to run
# https://svn.open-mpi.org/trac/ompi/ticket/4228
Requires:       openssh-clients

# Private openmpi libraries
%global __provides_exclude_from %{_libdir}/openmpi/lib/(lib(mca|ompi|open-(pal|rte|trace))|openmpi/).*.so
%global __requires_exclude lib(mca|ompi|open-(pal|rte|trace)|vt).*

%description
Open MPI is an open source, freely available implementation of both the
MPI-1 and MPI-2 standards, combining technologies and resources from
several other projects (FT-MPI, LA-MPI, LAM/MPI, and PACX-MPI) in
order to build the best MPI library available.  A completely new MPI-2
compliant implementation, Open MPI offers advantages for system and
software vendors, application developers, and computer science
researchers. For more information, see http://www.open-mpi.org/ .

%package devel
Summary:	Development files for openmpi
Requires:	%{name} = %{version}-%{release}, gcc-gfortran
Provides:	mpi-devel
%if !0%{?el7}
Requires:	rpm-mpi-hooks
# Make sure this package is rebuilt with correct Python version when updating
# Otherwise mpi.req from rpm-mpi-hooks doesn't work
# https://bugzilla.redhat.com/show_bug.cgi?id=1705296
Requires:	(python(abi) = %{python3_version} if python3)
%endif

%description devel
Contains development headers and libraries for openmpi.

%package doc
Summary:        HTML documentation for openmpi
BuildArch:      noarch

%description doc
HTML documentation for openmpi.

%if %{with java}
%package java
Summary:        Java library
Requires:       %{name} = %{version}-%{release}
Requires:       java-headless

%description java
Java library.

%package java-devel
Summary:        Java development files for openmpi
Requires:       %{name}-java = %{version}-%{release}
Requires:       java-devel

%description java-devel
Contains development wrapper for compiling Java with openmpi.
%endif

# We set this to for convenience, since this is the unique dir we use for this
# particular package, version, compiler
%global namearch openmpi-%{_arch}%{?_cc_name_suffix}

%if %{with python2}
%package -n python2-openmpi
Summary:        OpenMPI support for Python 2
BuildRequires:  python2-devel
Requires:       %{name} = %{version}-%{release}
Requires:       python(abi) = %{python2_version}

%description -n python2-openmpi
OpenMPI support for Python 2.
%endif

%package -n python%{python3_pkgversion}-openmpi
Summary:        OpenMPI support for Python 3
Requires:       %{name} = %{version}-%{release}
Requires:       python(abi) = %{python3_version}

%description -n python%{python3_pkgversion}-openmpi
OpenMPI support for Python 3.


%prep
%autosetup -p1 -n %{name}-%{version}
%if %{with autogen}
./autogen.pl --force
%endif


%build
%set_build_flags
./configure --prefix=%{_libdir}/%{name} \
	--mandir=%{_mandir}/%{namearch} \
	--includedir=%{_includedir}/%{namearch} \
	--sysconfdir=%{_sysconfdir}/%{namearch} \
	--disable-silent-rules \
	--enable-builtin-atomics \
	--enable-ipv6 \
%if %{with java}
	--enable-mpi-java \
%endif
	--enable-mpi1-compatibility \
%if %{with sphinx}
	--enable-sphinx \
%endif
	--with-prrte=external \
	--with-sge \
%ifarch %{valgrind_arches}
	--with-valgrind \
	--enable-memchecker \
%endif
	--with-hwloc=/usr \
%if !0%{?el7}
	--with-libevent=external \
%if %{with pmix}
	--with-pmix=external \
%endif
%endif

%make_build V=1

%install
%make_install
find %{buildroot}%{_libdir}/%{name}/lib -name \*.la | xargs rm
find %{buildroot}%{_mandir}/%{namearch} -type f | xargs gzip -9

# Make the environment-modules file
mkdir -p %{buildroot}%{_datadir}/modulefiles/mpi
# Since we're doing our own substitution here, use our own definitions.
sed 's#@LIBDIR@#%{_libdir}/%{name}#;
     s#@ETCDIR@#%{_sysconfdir}/%{namearch}#;
     s#@FMODDIR@#%{_fmoddir}/%{name}#;
     s#@INCDIR@#%{_includedir}/%{namearch}#;
     s#@MANDIR@#%{_mandir}/%{namearch}#;
%if %{with python2}
     s#@PY2SITEARCH@#%{python2_sitearch}/%{name}#;
%else
     /@PY2SITEARCH@/d;
%endif
     s#@PY3SITEARCH@#%{python3_sitearch}/%{name}#;
     s#@COMPILER@#openmpi-%{_arch}%{?_cc_name_suffix}#;
     s#@SUFFIX@#%{?_cc_name_suffix}_openmpi#' \
     <%{SOURCE1} \
     >%{buildroot}%{_datadir}/modulefiles/mpi/%{namearch}

# make the rpm config file
install -Dpm 644 %{SOURCE4} %{buildroot}/%{macrosdir}/macros.%{namearch}

# Link the fortran module to proper location
mkdir -p %{buildroot}%{_fmoddir}/%{name}
for mod in %{buildroot}%{_libdir}/%{name}/lib/*.mod
do
  modname=$(basename $mod)
  ln -s ../../../%{name}/lib/${modname} %{buildroot}/%{_fmoddir}/%{name}/
done

# Link the pkgconfig files into the main namespace as well
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cd %{buildroot}%{_libdir}/pkgconfig
ln -s ../%{name}/lib/pkgconfig/*.pc .
cd -

# Create cmake dir
mkdir -p %{buildroot}%{_libdir}/%{name}/lib/cmake/

# Create directories for OpenMPI packages with development files
mkdir -p %{buildroot}%{_libdir}/%{name}/lib/openmpi/cmake
mkdir -p %{buildroot}%{_libdir}/%{name}/include

# Remove extraneous wrapper link libraries (bug 814798)
sed -i -e s/-ldl// -e s/-lhwloc// \
  %{buildroot}%{_libdir}/%{name}/share/openmpi/*-wrapper-data.txt

# install .pth files
%if %{with python2}
mkdir -p %{buildroot}/%{python2_sitearch}/%{name}
install -pDm0644 %{SOURCE2} %{buildroot}/%{python2_sitearch}/openmpi.pth
%endif
mkdir -p %{buildroot}/%{python3_sitearch}/%{name}
install -pDm0644 %{SOURCE3} %{buildroot}/%{python3_sitearch}/openmpi.pth

%check
fail=1
make check || ( cat test/*/test-suite.log && exit $fail )

%files
%license LICENSE
%dir %{_libdir}/%{name}
%dir %{_sysconfdir}/%{namearch}
%dir %{_libdir}/%{name}/bin
%dir %{_libdir}/%{name}/lib
%dir %{_libdir}/%{name}/lib/openmpi
%dir %{_libdir}/%{name}/lib/openmpi/cmake
%dir %{_libdir}/%{name}/include
%dir %{_mandir}/%{namearch}
%dir %{_mandir}/%{namearch}/man*
%config(noreplace) %{_sysconfdir}/%{namearch}/*
%{_libdir}/%{name}/bin/mpi[er]*
%{_libdir}/%{name}/bin/ompi*
%if %{with ucx}
%{_libdir}/%{name}/bin/oshmem_info
%endif
%{_libdir}/%{name}/bin/oshrun
%if %{without pmix}
%{_libdir}/%{name}/bin/pattrs
%{_libdir}/%{name}/bin/pctrl
%{_libdir}/%{name}/bin/pevent
%{_libdir}/%{name}/bin/plookup
%{_libdir}/%{name}/bin/pmix_info
%{_libdir}/%{name}/bin/pmixcc
%{_libdir}/%{name}/bin/pps
%{_libdir}/%{name}/bin/pquery
%{_libdir}/%{name}/lib/libpmix.so.2*
%{_libdir}/%{name}/lib/pmix/
%{_libdir}/%{name}/share/pmix/
%{_mandir}/%{namearch}/man1/pmix_info.1*
%{_mandir}/%{namearch}/man5/openpmix.5*
%endif
%{_mandir}/%{namearch}/man7/Open-MPI.7*
%{_libdir}/%{name}/lib/*.so.40*
%{_libdir}/%{name}/lib/*.so.80*
%if 0%{?el7}
%{_libdir}/%{name}/lib/pmix/
%endif
%{_mandir}/%{namearch}/man1/mpirun.1*
%{_mandir}/%{namearch}/man1/mpisync.1*
%{_mandir}/%{namearch}/man1/ompi*
%if %{with ucx}
%{_mandir}/%{namearch}/man1/oshmem_info*
%endif
%{_libdir}/%{name}/lib/openmpi/*
%{_datadir}/modulefiles/mpi/
%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/openmpi
%{_libdir}/%{name}/share/openmpi/amca-param-sets
%{_libdir}/%{name}/share/openmpi/help*.txt
%if 0%{?el7}
%{_libdir}/%{name}/share/pmix/
%endif

%files devel
%dir %{_includedir}/%{namearch}
%{_libdir}/%{name}/bin/mpi[cCf]*
%{_libdir}/%{name}/bin/opal_*
%if %{with ucx}
%{_libdir}/%{name}/bin/osh[cCf]*
%endif
%if %{with ucx}
%{_libdir}/%{name}/bin/shmem[cCf]*
%endif
%{_includedir}/%{namearch}/*
%{_fmoddir}/%{name}/
%{_libdir}/%{name}/lib/*.so
%{_libdir}/%{name}/lib/*.mod
%{_libdir}/%{name}/lib/cmake/
%{_libdir}/%{name}/lib/pkgconfig/
%{_libdir}/pkgconfig/*.pc
%{_mandir}/%{namearch}/man1/mpi[cCf]*
%if %{with ucx}
%{_mandir}/%{namearch}/man1/osh[cCf]*
%{_mandir}/%{namearch}/man1/oshmem-wrapper-compiler.1*
%{_mandir}/%{namearch}/man1/shmem[cCf]*
%endif
%{_mandir}/%{namearch}/man1/opal_*
%{_mandir}/%{namearch}/man3/*
%{_libdir}/%{name}/share/openmpi/openmpi-valgrind.supp
%{_libdir}/%{name}/share/openmpi/*-wrapper-data.txt
%{macrosdir}/macros.%{namearch}

%files doc
%license LICENSE
%doc %{_libdir}/%{name}/share/doc/
%exclude %{_libdir}/%{name}/share/doc/openmpi/javadoc-openmpi

%if %{with java}
%files java
%{_libdir}/%{name}/lib/mpi.jar

%files java-devel
%{_libdir}/%{name}/bin/mpijavac
%{_libdir}/%{name}/bin/mpijavac.pl
%doc %{_libdir}/%{name}/share/doc/openmpi/javadoc-openmpi
%{_mandir}/%{namearch}/man1/mpijavac.1.gz
%endif

%if %{with python2}
%files -n python2-openmpi
%dir %{python2_sitearch}/%{name}
%{python2_sitearch}/openmpi.pth
%endif

%files -n python%{python3_pkgversion}-openmpi
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/openmpi.pth


%changelog
%autochangelog
