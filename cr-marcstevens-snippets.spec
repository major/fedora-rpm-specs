%global commit b795c03b1982964fb91ffd57ce8112844efd3291
%global snapdate 20240120

Name:           cr-marcstevens-snippets
# Neither the repository as a whole nor the individual header-only libraries
# have ever been versioned or formally released.
%global snapinfo ^%{snapdate}git%{sub %{commit} 1 7}
Version:        0%{snapinfo}
Release:        %autorelease
Summary:        Collection of useful one-file C/C++ headers

# The entire source is MIT except:
#
# • BSL-1.0:
#     cxxheaderonly/progress_display.hpp
#
# The BSL-1.0 source appears only in the
# cr-marcstevens-snippets-progress_display-devel subpackage.
#
# Additionally, the following are removed in %%prep and do not contribute to
# the binary RPMs:
#
# • FSFAP:
#     autoconf/*.m4, except as otherwise noted
# • GPL-3.0-or-later WITH Autoconf-exception-macro:
#     autoconf/ax_check_compile_flag.m4
#     autoconf/ax_prefix_config_h.m4
#     autoconf/ax_pthread.m4
# • GPL-2.0-or-later WITH Autoconf-exception-generic:
#     autoconf/ax_cuda.m4
License:        MIT AND BSL-1.0
URL:            https://github.com/cr-marcstevens/snippets
Source0:        %{url}/archive/%{commit}/snippets-%{commit}.tar.gz
# License URL referenced in cxxheaderonly/progress_display.hpp, converted from
# HTTP to HTTPS; see also:
#   Please add Boost license text
#   https://github.com/cr-marcstevens/snippets/issues/3
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/#_license_text
Source1:        https://www.boost.org/LICENSE_1_0.txt

# Replace using declaration with typedef
# https://github.com/cr-marcstevens/snippets/pull/2
Patch:          %{url}/pull/2.patch

# For compile-only “smoke tests”:
BuildRequires:  gcc-c++

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%description
%{summary}.


%package base64-devel
Summary:        A header only C++ base64 encoder/decoder library
License:        MIT

BuildArch:      noarch

Provides:       %{name}-base64-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description base64-devel
%{summary}.


%package concurrent_unordered_map-devel
Summary:        A header only C++ light-weight concurrent unordered map
License:        MIT

BuildArch:      noarch

Provides:       %{name}-concurrent_unordered_map-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description concurrent_unordered_map-devel
%{summary}.


%package cpuperformance-devel
Summary:        A header only C++ light-weight aids for CPU cycle counting
License:        MIT

BuildArch:      noarch

Provides:       %{name}-cpuperformance-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description cpuperformance-devel
%{summary}.


%package parallel_algorithms-devel
Summary:        A header only C++ light-weight parallel algorithms library
License:        MIT

BuildArch:      noarch

Provides:       %{name}-parallel_algorithms-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description parallel_algorithms-devel
%{summary}.


%package program_options-devel
Summary:        A header only C++ C++ boost-like program options class
License:        MIT

BuildArch:      noarch

Provides:       %{name}-program_options-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description program_options-devel
%{summary}.


%package progress_display-devel
Summary:        Extension from boost::progress_display
# This contains *only* cxxheaderonly/progress_display.hpp, without any of the
# MIT-licensed sources.
License:        BSL-1.0

BuildArch:      noarch

Provides:       %{name}-progress_display-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description progress_display-devel
%{summary}.


%package string_algo-devel
Summary:        A header only C++ string algorithms
License:        MIT

BuildArch:      noarch

Provides:       %{name}-string_algo-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description string_algo-devel
%{summary}.


%package thread_pool-devel
Summary:        A header only C++ light-weight thread pool
License:        MIT

BuildArch:      noarch

Provides:       %{name}-thread_pool-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description thread_pool-devel
%{summary}.


%prep
%autosetup -n snippets-%{commit} -p1
# We are not packaging these, and many have licenses that are acceptable for
# packaging but differ from those listed in the License field. To keep things
# clean, we remove them.
rm -rvf autoconf
# Please add Boost license text
# https://github.com/cr-marcstevens/snippets/issues/3
cp -p '%{SOURCE1}' .


%build
# There is no compiled code to install, since all libraries are header-only. We
# do do a compile-only “smoke test” for each library.
%set_build_flags
mkdir -p _test '%{_vpath_builddir}'
for hdr in cxxheaderonly/*.hpp
do
  lib="$(basename "${hdr}" '.hpp')"
  cat > "_test/${lib}.cpp" <<EOF
#include "${lib}.hpp"
int main(int, char *[]) { return 0; }
EOF
  "${CXX:-g++}" -I"${PWD}/cxxheaderonly" "_test/${lib}.cpp" \
      -o "%{_vpath_builddir}/${lib}" ${CXXFLAGS} ${LDFLAGS}
done


%install
install -t '%{buildroot}%{_includedir}/cr-marcstevens' \
    -p -m 0644 -D cxxheaderonly/*.hpp


# Upstream has no tests.


%files base64-devel
%license LICENSE
# Shared base directory
%dir %{_includedir}/cr-marcstevens
%{_includedir}/cr-marcstevens/base64.hpp


%files concurrent_unordered_map-devel
%license LICENSE
# Shared base directory
%dir %{_includedir}/cr-marcstevens
%{_includedir}/cr-marcstevens/concurrent_unordered_map.hpp


%files cpuperformance-devel
%license LICENSE
# Shared base directory
%dir %{_includedir}/cr-marcstevens
%{_includedir}/cr-marcstevens/cpuperformance.hpp


%files parallel_algorithms-devel
%license LICENSE
# Shared base directory
%dir %{_includedir}/cr-marcstevens
%{_includedir}/cr-marcstevens/parallel_algorithms.hpp


%files program_options-devel
%license LICENSE
# Shared base directory
%dir %{_includedir}/cr-marcstevens
%{_includedir}/cr-marcstevens/program_options.hpp


%files progress_display-devel
%license LICENSE_1_0.txt
# Shared base directory
%dir %{_includedir}/cr-marcstevens
%{_includedir}/cr-marcstevens/progress_display.hpp


%files string_algo-devel
%license LICENSE
# Shared base directory
%dir %{_includedir}/cr-marcstevens
%{_includedir}/cr-marcstevens/string_algo.hpp


%files thread_pool-devel
%license LICENSE
# Shared base directory
%dir %{_includedir}/cr-marcstevens
%{_includedir}/cr-marcstevens/thread_pool.hpp


%changelog
%autochangelog
