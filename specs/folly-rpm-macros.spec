Name:           folly-rpm-macros
Version:        46
Release:        %autorelease
Summary:        RPM macros for building Meta's C++ projects with getdeps

License:        MIT
URL:            https://src.fedoraproject.org/rpms/folly-rpm-macros
Source0:        macros.folly-rpm
Source1:        getdeps_vendor.attr
Source2:        getdeps_vendor.prov
Source3:        getdeps_vendor_license_check

BuildArch:      noarch

Requires:       rpm
# the %%getdeps_* macros run getdeps.py with %%{__python3}
Requires:       python3
# %%getdeps_install runs %%{__cmake}
Requires:       cmake-rpm-macros
# getdeps applies a manifest's patchfile with `git apply`, so a build needs
# git whenever it builds a project that has one. Fedora buildroots happen to
# have it; EPEL 10's do not, and there the vendored glog (which carries a
# patchfile) made the build fail with FileNotFoundError: 'git'.
Requires:       git-core
# the %%getdeps_vendor_license_* macros wrap go_vendor_license and licensecheck
Requires:       go-vendor-tools
# licensecheck is Fedora-only (no EPEL build of it); without it the check
# macro's -f pass reports that it is unavailable and verifies the License tag
# against the license files alone, which is what EPEL builds get.
%if 0%{?fedora}
Requires:       licensecheck
%endif
# the %%folly_toolchain macro and its subpackage were dropped in 46; nothing used them
Obsoletes:      folly-srpm-macros < 46

%description
folly-rpm-macros contains the %%getdeps_* macros for building Meta's C++
projects (cachelib, mcrouter, ...) with build/fbcode_builder/getdeps.py from
system packages plus a vendored tree of the remaining dependencies (folly,
fizz, wangle, mvfst, fbthrift, ...), and the file attributes that turn the
vendored tree into bundled() Provides.


%prep


%build


%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE0}
install -D -p -m 0644 -t %{buildroot}%{_fileattrsdir} %{SOURCE1}
install -D -p -m 0755 -t %{buildroot}%{_rpmconfigdir} %{SOURCE2} %{SOURCE3}


%files
%{_rpmmacrodir}/macros.folly-rpm
%{_fileattrsdir}/getdeps_vendor.attr
%{_rpmconfigdir}/getdeps_vendor.prov
%{_rpmconfigdir}/getdeps_vendor_license_check


%changelog
%autochangelog
