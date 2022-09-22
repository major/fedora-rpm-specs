%global commit 814e3418cf65bb240f61528ed1c01f7a48c3a22e
%global snapdate 20220724

%global shortcommit %(echo '%{commit}' | cut -b -7)

Name:           geompp
Summary:        Basic geometrical utilities for C++
# Upstream has never chosen a version
Version:        0^%{snapdate}git%{shortcommit}
Release:        %autorelease -p

License:        GPL-3.0-or-later
URL:            https://github.com/monocasual/geompp
Source0:        %{url}/archive/%{commit}/geompp-%{commit}.tar.gz

BuildRequires:  gcc-c++

# This package is header-only, so the binary RPMs do not include any compiled
# executables.
%global debug_package %{nil}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package devel
Summary:        %{summary}

BuildArch:      noarch

# Header-only library
Provides:       geompp-static = %{version}-%{release}

%description devel %{common_description}


%prep
%autosetup -n geompp-%{commit}
# Patch to allow installing in a subdirectory of the global include path
# https://github.com/monocasual/geompp/issues/1
sed -r -i 's|^(#include ")([^/]+\.hpp")|\1geompp/\2|' src/*.hpp

# As a “smoke test”, create a source file that includes all of the API headers,
# and verify that we can compile and link it.
mkdir -p smoke_test
ln -s ../src/ smoke_test/geompp
cat > smoke_test/include_all.cpp <<EOF
$(find src -type f -name '*.hpp' -printf '#include "geompp/%%P"\n')
int main(int argc, char * argv[]) { (void) argc; (void) argv; return 0; }
EOF

%build
# No build section required for this header-only library

# “Smoke test” that verifies we can at least compile and link a source that
# includes the headers. There is no need to run the resulting executable, which
# does nothing.
%set_build_flags
mkdir -p '%{_vpath_builddir}/smoke_test'
${CXX} -Ismoke_test ${CPPFLAGS} ${LDFLAGS} \
    -o '%{_vpath_builddir}/smoke_test/include_all' \
    smoke_test/include_all.cpp


# Upstream has no tests, and our “smoke test” is satisfied by a successful
# %%build, so there is no %%check.


%install
install -t '%{buildroot}%{_includedir}/geompp' -D -m 0644 -p src/*.hpp


%files devel
%license LICENSE

%{_includedir}/geompp


%changelog
%autochangelog
