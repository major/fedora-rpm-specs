%global _lto_cflags %{nil}

%global srcname pyfastnoisesimd

Name:           python-%{srcname}
Version:        0.4.2
Release:        11%{?dist}
Summary:        Python Fast Noise with SIMD

License:        BSD-3-Clause
URL:            http://github.com/robbmcleod/pyfastnoisesimd
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
# https://github.com/Auburns/FastNoiseSIMD/commit/32873404111701397781fe9ef21931fed4f7f766
# https://github.com/Auburns/FastNoiseSIMD/commit/575c0047bbfd2bac841359daa9db220a9f97a638
# https://github.com/Auburns/FastNoiseSIMD/pull/27
Patch0001:      0001-Update-casts-for-NEON.patch
# https://github.com/Auburns/FastNoiseSIMD/pull/31
Patch0002:      0002-Use-fallback-for-PPC64-and-S390x.patch
# https://github.com/robbmcleod/pyfastnoisesimd/pull/15
Patch0003:      0003-Add-platform-specific-flags-for-NEON.patch
# https://github.com/Auburns/FastNoiseSIMD/pull/32
Patch0004:      0004-Use-getauxval-to-check-for-NEON-on-Linux.patch
# https://github.com/robbmcleod/pyfastnoisesimd/pull/25
Patch0005:      0005-Fix-alignment-on-non-optimized-systems-in-tests.patch

# gcc seems to enable SSE2 even when not requested.
ExcludeArch:   %{ix86}

%global _description \
PyFastNoiseSIMD is a wrapper around Jordan Peck's synthetic noise library which \
has been accelerated with SIMD instruction sets. \
\
Parallelism is further enhanced by the use of concurrent.futures to \
multi-thread the generation of noise for large arrays. Thread scaling is \
generally in the range of 50-90%, depending largely on the vectorized \
instruction set used. The number of threads, defaults to the number of virtual \
cores on the system.

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 34.1
BuildRequires:  python3dist(numpy) > 1.7

Requires:       python3dist(numpy) > 1.7

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
mkdir empty
pushd empty
PYTHONPATH="%{buildroot}%{python3_sitearch}" \
    %{python3} -c "import sys; import pyfastnoisesimd; sys.exit(0 if pyfastnoisesimd.test().wasSuccessful() else 1)"
popd


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.2-9
- Rebuilt for Python 3.12

* Sat Apr 08 2023 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.2-8
- Switch to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.2-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.10

* Wed Mar 31 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.2-1
- Update to latest version (#1944953)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-9
- Disable LTO

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-1
- Update to latest version

* Fri Jul 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Initial package.
