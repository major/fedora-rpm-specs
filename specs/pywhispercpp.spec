%global pypi_name pywhispercpp
%global whispercpp_version 1.8.2

Name:           %{pypi_name}
Version:        1.4.0
Release:        2%{?dist}
Summary:        Python bindings for whisper.cpp with a simple Pythonic API
# Architecture-specific due to C/C++ extensions
ExcludeArch: %{ix86}
License:        MIT
URL:            https://github.com/absadiki/pywhispercpp
Source0:        %{pypi_source}
Source1:        https://github.com/ggml-org/whisper.cpp/archive/refs/tags/v%{whispercpp_version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  chrpath
BuildRequires:  pybind11-devel
BuildRequires:  python3-pytest
Provides: bundled(whisper.cpp) = %{whispercpp_version}

%description
pywhispercpp provides Python bindings for whisper.cpp with a simple
Pythonic API on top of it.

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3-qt5
Provides:       pywhispercpp = %{version}-%{release}

%description -n python3-%{pypi_name}
pywhispercpp provides Python bindings for whisper.cpp with a simple
Pythonic API on top of it.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# pybind11 is replaced with system available pybind11-devel
rm -rf pybind11
sed -i 's|add_subdirectory(pybind11)|find_package(pybind11 REQUIRED)|g' CMakeLists.txt

# Remove the whisper.cpp copy bundled in pywhispercpp sources and replace it with a 
# separately versioned whisper.cpp tarball
rm -rf whisper.cpp
tar -xzf %{SOURCE1}
mv whisper.cpp-%{whispercpp_version} whisper.cpp

# Remove shebang
find pywhispercpp -name "*.py" -exec sed -i '/^#!/d' {} \;
# Remove repairwheel from build dependencies as it is not available in fedora
sed -i 's/"repairwheel",//g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
# Enable Native CPU Optimizations for GGML 
export CMAKE_ARGS=" -DGGML_NATIVE=ON "
export NO_REPAIR=1
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name} _pywhispercpp

# Remove rpath from libraries
chrpath --replace '$ORIGIN' %{buildroot}%{python3_sitearch}/_pywhispercpp*.so
chrpath --replace '$ORIGIN' %{buildroot}%{python3_sitearch}/libggml-cpu.so
chrpath --replace '$ORIGIN' %{buildroot}%{python3_sitearch}/libggml.so
chrpath --replace '$ORIGIN' %{buildroot}%{python3_sitearch}/libwhisper.so.1

# Remove unversioned and full-version libwhisper symlinks installed by upstream
# only libwhisper.so.1 is kept for runtime use
rm -rf %{buildroot}%{python3_sitearch}/libwhisper.so
rm -rf %{buildroot}%{python3_sitearch}/libwhisper.so.%{whispercpp_version}

# Removed below binaries as these require python-sounddevice & python-ffmpeg packages (missing in fedora)
rm -rf %{buildroot}%{_bindir}/pwcpp-assistant
rm -rf %{buildroot}%{_bindir}/pwcpp-recording
rm -rf %{buildroot}%{_bindir}/pwcpp-livestream

%check
# Not importing examples as it requires python-sounddevice & python-ffmpeg packages (missing in fedora)
%pyproject_check_import -e "pywhispercpp.examples*"
# Only run test_c_api.py as other tests require downloading models from internet
%pytest -v tests/test_c_api.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/pwcpp*
%{python3_sitearch}/libggml*.so
%{python3_sitearch}/libwhisper.so.1

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Dec 17 2025 Manish Tiwari <matiwari@redhat.com> - 1.4.0-1
- Update to 1.4.0 version
- Bundled whisper.cpp
- Remove pybind11 to use system available pybind11-devel

* Tue Dec 9 2025 Manish Tiwari <matiwari@redhat.com> - 1.3.3-1
- Initial import
