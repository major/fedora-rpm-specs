Name:           python-Rtree
Version:        1.0.0
Release:        4%{?dist}
Summary:        R-Tree spatial index for Python GIS

# Since the package has a history of arch-dependent bugs (see RHBZ#2055249),
# the base package is arched to flush out any arch-dependent bugs by ensuring
# the tests are run on every architecture. The binary package is still
# pure-Python and correctly noarch. Since there is no compiled code, there is
# no debuginfo to generate.
%global debug_package %{nil}

%global _description %{expand: \
Rtree is a ctypes Python wrapper of libspatialindex that provides a number of
advanced spatial indexing features for the spatially curious Python user. These
features include:

  • Nearest neighbor search
  • Intersection search
  • Multi-dimensional indexes
  • Clustered indexes (store Python pickles directly with index entries)
  • Bulk loading
  • Deletion
  • Disk serialization
  • Custom storage implementation (to implement spatial indexing in ZODB, for
    example)}

License:        LGPLv2
URL:            https://github.com/Toblerity/rtree
Source0:        %{pypi_source Rtree}

# Since we are not bundling libspatialindex as upstream does for PyPI wheel
# distribution, do not force setuptools to treat the package as binary/arched
# (which would cause it to be installed in %%python3_sitearch, and would mean
# this package could not properly be noarch).
#
# Since upstream does want to bundle libspatialindex, this is a downstream-only
# patch.
#
# https://bugzilla.redhat.com/show_bug.cgi?id=2050010
Patch0:         Rtree-1.0.0-no-bundled-spatialindex.patch

BuildRequires:  spatialindex-devel

BuildRequires:  python3-devel

# For testing:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)

%description %{_description}


%package -n python3-rtree
Summary:        %{summary}

BuildArch:      noarch

Requires:       spatialindex

%description -n python3-rtree %{_description}


%prep
%autosetup -n Rtree-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files rtree


%check
%pytest --doctest-modules


# Note that there is no %%files section for the unversioned python module if we
# are building for several python runtimes
%files -n python3-rtree -f %{pyproject_files}
# pyproject_files handles LICENSE.txt; verify with “rpm -qL -p …”
%doc README.md


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.11

* Sat Apr 16 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.0-2
- Fix spatialite→spatialindex typo in patch name/description

* Wed Apr 06 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.0-1
- Update to 1.0.0
- Tidy up spec file macros and other trivia
- Use pyproject-rpm-macros

* Sat Feb 19 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.7-4
- Ensure tests run on all architectures
- Fix RHBZ#2055249 with upstream PR#222, which includes fixes for additional C
  API mismatches.

* Thu Feb 03 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.7-3
- Fix arch/noarch confusion (fix RHBZ#2050010)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.7-1
- Update to 0.9.7

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.4-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-2
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Volker Fröhlich <volker27@gmx.at> - 0.9.4-1
- New version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Volker Fröhlich <volker27@gmx.at> - 0.9.3-1
- New version

* Mon Dec 09 2019 Volker Fröhlich <volker27@gmx.at> - 0.9.2-1
- New version

* Mon Nov 25 2019 Volker Fröhlich <volker27@gmx.at> - 0.9.1-1
- Remove meaningless comment
- There's no point in building documentation we don't ship and it failed too
- Remove outdated version constraints on R/BR
- Remove upstreamed patch

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.3-8
- Subpackage python2-rtree has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Volker Fröhlich <volker27@gmx.at> - 0.8.3-4
- Remove meaningless comment

* Thu Aug 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.3-4
- Rename binary packages to lowercase

* Sat Aug 12 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.8.3-3
- New upstream release
- Update spec to new guidelines
- Add Python 3 subpackage (#1481100)
- Add documentation
- Simplify spec with more macros
- NumPy is needed for testing as well

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 08 2014 Volker Fröhlich <volker27@gmx.at> - 0.7.0-5
- Remove hard-coded library extension (BZ#1001840)
- Ignore harmless test failure to fix FTBFS
- Remove obsolete version requirements

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Volker Fröhlich <volker27@gmx.at> - 0.7.0-2
- BR python-setuptools instead of ...-devel
- Delete pre-built egg info

* Sat Apr 14 2012 Volker Fröhlich <volker27@gmx.at> - 0.7.0-1
- Initial package for Fedora
