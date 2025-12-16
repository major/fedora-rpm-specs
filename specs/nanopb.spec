%bcond_without check

%global forgeurl https://github.com/nanopb/nanopb
Version:        0.4.9.1
%global tag %{version}
%forgemeta

Name:           nanopb
Release:        %autorelease
Summary:        A small code-size Protocol Buffers implementation in ansi C
License:        Zlib
URL:            https://jpa.kapsi.fi/nanopb/
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
# for testing
%if %{with check}
BuildRequires:  python3-scons
BuildRequires:  %{py3_dist grpcio-tools}
%endif

%description
Nanopb is a small code-size Protocol Buffers implementation in ansi C. It is
especially suitable for use in microcontrollers, but fits any memory restricted
system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        python3
Summary:        Small code-size Protocol Buffers implementation in Python
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    python3
The %{name}-python3 package contains Small code-size Protocol Buffers
implementation in Python. It includes the protoc-based generator, which converts
.proto files to .pb.h files for inclusion in a project.

%prep
%forgeautosetup -p1

# remove unneeded files
rm generator/{nanopb_generator.py2,protoc-gen-nanopb-py2}
rm generator/*.bat

# https://github.com/nanopb/nanopb/blob/master/extra/poetry/poetry_build.sh
cp extra/poetry/pyproject.toml .
mkdir -p nanopb
cp -r generator nanopb
touch nanopb/__init__.py nanopb/generator/__init__.py
make -C nanopb/generator/proto

%generate_buildrequires
%pyproject_buildrequires

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_STATIC_LIBS=OFF \
    -Dnanopb_BUILD_GENERATOR=OFF \

%cmake_build

%pyproject_wheel

%install
%cmake_install

%pyproject_install
%pyproject_save_files nanopb

%if %{with check}
%check
pushd tests
    scons
popd
%endif

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libprotobuf-nanopb.so.0

%files devel
%{_libdir}/libprotobuf-nanopb.so
%{_includedir}/nanopb/
%dir %{_libdir}/cmake/nanopb
%{_libdir}/cmake/nanopb/*.cmake

%files python3 -f %{pyproject_files}
%{_bindir}/nanopb_generator
%{_bindir}/protoc-gen-nanopb

%changelog
%autochangelog
