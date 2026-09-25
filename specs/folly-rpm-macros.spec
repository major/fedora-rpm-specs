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
# the %%getdeps_vendor_license_* macros wrap go_vendor_license and licensecheck
Requires:       go-vendor-tools
Requires:       licensecheck
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
