# Copyright (c) 2014, 2015  Dave Love, University of Liverpool
# Copyright (c) 2018, 2019  Dave Love, University of Manchester
# MIT licence, per Fedora policy.

# fixme: appdata/desktop files?
# fixme: make common package with non-MPI-specific contents

%bcond_without mpich

%global shortver %(echo %version|awk -F. '{print $1 "." $2}')

Name:		scalasca
Version:	2.6.1
Release:	8%{?dist}
Summary:	Toolset for performance analysis of large-scale parallel applications

# ScoutPatternParser and SilasConfigParser are Bison-generated
License:	BSD-3-Clause AND GPL-3.0-or-later WITH Bison-exception-2.2
URL:		http://www.scalasca.org/
Source0:	http://apps.fz-juelich.de/scalasca/releases/scalasca/%shortver/dist/%name-%version.tar.gz
BuildRequires: make
BuildRequires:	otf2-devel >= 3.0, cube-devel >= 4.8
BuildRequires:	zlib-devel openmpi-devel chrpath gcc-c++
%if %{with mpich}
BuildRequires:	mpich-devel
%endif
Requires:	scorep-config
# As for scorep
ExcludeArch: s390 s390x armv7hl i686

%global desc \
Scalasca is a software tool that supports the performance optimization\
of parallel programs by measuring and analyzing their runtime\
behavior. The analysis identifies potential performance bottlenecks –\
in particular those concerning communication and synchronization – and\
offers guidance in exploring their causes.\
\
Scalasca targets mainly scientific and engineering applications based\
on the programming interfaces MPI and OpenMP, including hybrid\
applications based on a combination of the two. The tool has been\
specifically designed for use on large-scale systems, but is also well\
suited for small- and medium-scale HPC platforms.

%description
%desc

%package openmpi
Summary:	Toolset for performance analysis of large-scale parallel applications - openmpi
Requires:	openmpi%{?_isa}
Requires:	scorep-openmpi-config

%description openmpi
%desc

%if 0%{?el7}
%package openmpi3
Summary:	Toolset for performance analysis of large-scale parallel applications - openmpi3
BuildRequires:	openmpi3-devel
Requires:	openmpi3%{?_isa}
Requires:	scorep-openmpi3-config

%description openmpi3
%desc

This is the openmpi3 version.
%endif

%if %{with mpich}
%package mpich
Summary:	Toolset for performance analysis of large-scale parallel applications - mpich
Requires:	mpich%{?_isa}
Requires:	scorep-mpich-config

%description mpich
%desc

This is the mpich version.
%endif

%package doc
Summary: Documentation for %name
BuildArch: noarch

%description doc
Documentation for %name

%prep
%setup -q
mkdir openmpi mpich simple %{?el7:openmpi3}
rm -r vendor/cubew vendor/otf2	# bundled libraries


%build
%global _configure ../configure
%global do_build \
%configure --with-otf2 --with-cube --enable-shared --libdir=$MPI_LIB \\\
	   --bindir=$MPI_BIN --datadir=$MPI_HOME/share LDFLAGS=-Wl,--as-needed \\\
	   --enable-backend-test-runs --disable-silent-rules \\\
	   --mandir=$MPI_MAN --docdir=%_pkgdocdir \
	   %make_build
pushd openmpi
%_openmpi_load
%do_build
%_openmpi_unload
popd
%if 0%{?el7}
pushd openmpi3
%_openmpi3_load
%do_build
%_openmpi3_unload
popd
%endif
%if %{with mpich}
pushd mpich
%_mpich_load
%do_build
%_mpich_unload
popd
%endif
pushd simple
%configure --with-otf2 --with-cube --enable-shared LDFLAGS=-Wl,--as-needed \
	   --enable-backend-test-runs --disable-silent-rules --without-mpi \
	   --docdir=%_pkgdocdir
%make_build
popd


%install
%make_install -C openmpi
%{?el7:%make_install -C openmpi3}
%if %{with mpich}
%make_install -C mpich
%endif
%make_install -C simple

find $RPM_BUILD_ROOT%_libdir \( -name \*.la -o -name \*.a \) -exec rm -f {} \;
chrpath -d $RPM_BUILD_ROOT%_bindir/scout.{ser,omp}
chrpath -d $RPM_BUILD_ROOT%_libdir/{openmpi,mpich}/bin/scout.{ser,omp}


%check
%_openmpi_load
cd openmpi
OMPI_MCA_rmaps_base_oversubscribe=1 \
make check VERBOSE=1


%ldconfig_scriptlets

%files
%doc README
%license COPYING
%_datadir/%name
%exclude %_libdir/*.so
%_libdir/*.so.*
%_bindir/*
%_mandir/man1/*

%files openmpi
%doc README
%license COPYING
%_libdir/openmpi/share/%name
%exclude %_libdir/openmpi/lib/*.so
%_libdir/openmpi/lib/*.so.*
%_libdir/openmpi/bin/*
%_mandir/openmpi-*/man1/*

%if 0%{?el7}
%files openmpi3
%doc README
%license COPYING
%_libdir/openmpi3/share/%name
%exclude %_libdir/openmpi3/lib/*.so
%_libdir/openmpi3/lib/*.so.*
%_libdir/openmpi3/bin/*
%_mandir/openmpi3-*/man1/*
%endif

%if %{with mpich}
%files mpich
%doc README
%license COPYING
%_libdir/mpich/share/%name
%exclude %_libdir/mpich/lib/*.so
%_libdir/mpich/lib/*.so.*
%_libdir/mpich/bin/*
%_mandir/mpich*/man1/*
%endif

%files doc
%license COPYING
%_pkgdocdir


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Jan Kolarik <jkolarik@redhat.com> - 2.6.1-5
- Switch scorep-config file dependencies for packages (rhbz#2229953)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 2.6.1-4
- Rebuild for openmpi 5.0.0, drops C++ API

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Dave Love <loveshack@fedoraproject.org> - 2.6.1-1
- New version (#2153767)

* Thu Sep  8 2022 Dave Love <loveshack@fedoraproject.org> - 2.6-5
- Use SPDX licence TAG

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 20 2021 Dave Love <loveshack@fedoraproject.org> - 2.6-1
- New version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep  3 2019 Dave love <loveshack@fedoraproject.org> - 2.5-3
- Modify for el7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 2019 Dave Love <loveshack@fedoraproject.org> - 2.5-1
- New version
- Drop patch
- Adjust doc files

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2.4-7
- Rebuild for openmpi 3.1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Dave Love <loveshack@fedoraproject.org> - 2.4-5
- Require scorep-config, not .spec file
- BR cube-devel >= 4.4

* Sat Oct 27 2018 Dave Love <loveshack@fedoraproject.org> - 2.4-4
- Correct dependence on scorep.spec

* Wed Oct 24 2018 Dave Love <loveshack@fedoraproject.org> - 2.4-3
- Require scorep config [#1610849]
- Fix finding scorep.spec in square
- Some rpm spec cleanup

* Sat Jul 21 2018 Dave Love <loveshack@fedoraproject.org> - 2.4-2
- BR gcc-c++ (#1606306)
- Remove unnecessary -std=gnu++98

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Dave Love <loveshack@fedoraproject.org> - 2.4-1
- New version (#1578180)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.1-2
- Rebuild for openmpi 2.0

* Fri May 20 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.1-1
- Update to 2.3.1
- Drop pearl patch applied upstream

* Thu May 12 2016 Dave Love <loveshack@fedoraproject.org> - 2.3-4
- Run ldconfig for main package too, and fix rpath

* Wed May 11 2016 Dave Love <loveshack@fedoraproject.org> - 2.3-3
- Build non-MPI version
  Resolves: rhbz#1334560
- Use separate datadirs; at least summary file is build-dependent

* Sat Apr 16 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3-2
- Just fix test program linkage

* Fri Apr 15 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3-1
- Update to 2.3
- Add patch to fix libpearl_base linkage

* Sun Feb 14 2016 Dave Love <loveshack@fedoraproject.org> - 2.2.2-6
- Set CXX flags to build with gcc6
- Disable silent make rules

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.2-4
- Rebuild for openmpi 1.10.0

* Sat Aug 22 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.2-3
- BR openssh-clients so test works in koji epel7

* Tue Jul 7 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.2-2
- Various spec tidying
- Don't build devel package -- doesn't seem useful

* Thu Jun 25 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.2-1
- New version

* Thu May 28 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.1-1
- New version

* Sun Feb 22 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2-1
- New version

* Sun Feb 22 2015 Dave Love <d.love@liverpool.ac.uk> - 2.1-6
- Configure and run tests
- Avoid mpich on el6 ppc64
- Remove defattr

* Wed Dec 24 2014 Dave Love <d.love@liverpool.ac.uk> - 2.1-5
- Don't install .a files

* Tue Dec 16 2014 Dave Love <d.love@liverpool.ac.uk> - 2.1-4
- Modify requires

* Sun Dec 14 2014 Dave Love <d.love@liverpool.ac.uk> - 2.1-4
- Fix copyright

* Thu Dec 11 2014 Dave Love <d.love@liverpool.ac.uk> - 2.1-3
- Add mpich

* Thu Nov 20 2014 Dave Love <d.love@liverpool.ac.uk> - 2.1-2
- Minor rpmlint fixes

* Mon Oct 13 2014 Dave Love <d.love@liverpool.ac.uk> - 2.1-2
- Initial packaging
