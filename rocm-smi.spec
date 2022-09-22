Name:           rocm-smi
Version:        4.0.0
Release:        %autorelease
Summary:        AMD ROCm System Management Interface

License:        MIT
URL:            https://github.com/RadeonOpenCompute/ROC-smi
Source0:        https://github.com/RadeonOpenCompute/ROC-smi/archive/rocm-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  help2man

# Upstream deprecated this utility in the 3.9.0 release by renaming rocm_smi.py
# to rocm_smi_deprecated.py in the sample rpm and deb package builds. A comment
# in python_smi_tools/rocmSmiLib_cli.py from
# https://github.com/RadeonOpenCompute/rocm_smi_lib/ indicates that interface
# is supposed to replace this one. Since this tool is now unsupported, it will
# become less and less useful as time and hardware progress. It should be
# removed when and if the replacement tool is packaged.
Provides:       deprecated()

%description
This package includes the rocm-smi tool. This tool exposes functionality for
clock and temperature management of your ROCm enabled system.


%prep
%autosetup -n ROC-smi-rocm-%{version}


%build
# Generate a man page from the --help output.
help2man --version-string=%{version} --no-info --section=1 \
    --output=rocm-smi.1 ./rocm-smi
# Strip out ROCM-SMI and kernel version numbers that pertain to the build
# environment.
sed -r 's/[[:blank:]]+\|[[:blank:]].*version:.*$//' -i rocm-smi.1


%install
install -d %{buildroot}%{_bindir}
install rocm_smi.py %{buildroot}%{_bindir}/rocm-smi
install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -m 0644 rocm-smi.1


# We do not run the tests because they are not self-contained: they require
# particular hardware to be installed, issue commands to that hardware, and may
# require elevated privileges.


%files
%license LICENSE
%doc README.md
%{_bindir}/rocm-smi
%{_mandir}/man1/rocm-smi.1*


%changelog
%autochangelog
