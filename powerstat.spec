Name:           powerstat
Version:        0.03.03
Release:        1%{?dist}
Summary:        Measures the power consumption of a machine

License:        GPL-2.0-or-later
URL:            https://github.com/ColinIanKing/powerstat
Source:         %{url}/archive/V%{version}/%{name}-V%{version}.tar.gz
# Preserve timestamp of powerstat file and let build system
# compress man page
Patch:          01-preserve-timestamp-copy-man.patch

BuildRequires:  gcc
BuildRequires:  make
# RAPL not available on other architectures
ExclusiveArch:  %{ix86} x86_64

%description
Powerstat measures the power consumption of a machine using the
battery stats or the Intel RAPL interface. The output is like
vmstat but also shows power consumption statistics. At the end
of a run, powerstat will calculate the average, standard
deviation and min/max of the gathered data.


%prep
%autosetup


%build
# Preserve timestamp
%make_build


%install
%make_install


%check
# Smoke test binary works, no tests available
%{buildroot}%{_bindir}/powerstat -h


%files
%doc README.md
%license COPYING
%{_bindir}/powerstat
%{_mandir}/man8/powerstat.8*
%{bash_completions_dir}/powerstat



%changelog
* Fri Aug 25 2023 Benson Muite <benson_muite@emailplus.org> - 0.03.03-1
- Initial packaging
