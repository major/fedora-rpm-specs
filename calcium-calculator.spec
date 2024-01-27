%global forgeurl https://github.com/mvvik/CalC-complex-buffer

# Build with FreeGLUT
%bcond freeglut 1

Name:       calcium-calculator
Version:    7.10.6
Release:    %autorelease
Summary:    The Calcium Calculator
%global tag v%{version}
%forgemeta
# SPDX
License:    GPL-3.0-only
URL:        https://web.njit.edu/~matveev/calc.html
Source0:    %forgesource
# Use Makefile from v7.10.7 release
# Makefile in v7.10.6 uses Mac specific flags
Patch:      Makefile_v7.10.7.patch
# Use our build flags, which work on all arches.
# Most of the options set by upstream are included, except '-m64' and '-mtune'.
Patch:      include_local_CXXFLAGS.patch

BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  make
%if %{with freeglut}
BuildRequires:  freeglut-devel
%endif

%description
CalC ("Calcium Calculator") is a free (GNU copyleft) modeling tool for
simulating intracellular calcium diffusion and buffering. CalC solves
continuous reaction-diffusion PDEs describing the entry of calcium into a
volume through point-like channels, and its diffusion, buffering and binding to
calcium receptors.


%prep
%forgeautosetup -p1 -S git

find . -name "*" -type f -exec chmod 0644 '{}' \;
find . -name "*" -type f -exec sed -i 's/\r$//' '{}' \;

%build
%{set_build_flags}
%if %{with freeglut}
%make_build
%else
%make_build noGraphs
%endif

%install
# Rename to prevent conflict
mv -v CalC %{name}
install -p -m 755 -D -t $RPM_BUILD_ROOT/%{_bindir} %{name}


%files
%doc README.* examples
%{_bindir}/%{name}
# Yes, that's a typo, but not mine.
%license LIcense_gpl-3.0.txt

%changelog
%autochangelog
