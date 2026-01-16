# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

# Upstream has not tagged any releases
%global commit b1ef26a55cdb60d236a5cb199c4234c704f46726
%global date   20210314
%global forgeurl https://github.com/orlp/pdqsort

Name:           pdqsort
Version:        0
Summary:        Pattern-defeating quicksort library

%forgemeta

Release:        %autorelease
License:        Zlib
URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++

%global _desc %{expand:Pattern-defeating quicksort (pdqsort) is a novel sorting algorithm that
combines the fast average case of randomized quicksort with the fast worst
case of heapsort, while achieving linear time on inputs with certain patterns.
pdqsort is an extension and improvement of David Musser's introsort.}

%description
%_desc

%package        devel
Summary:        Pattern-defeating quicksort library
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%_desc

%prep
%forgeautosetup

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_includedir}
cp -p pdqsort.h %{buildroot}%{_includedir}

%check
# Run the benchmark as a kind of test, but only run small sizes
# This is only possible on x86_64 due to use of rdtsc
%ifarch %{x86_64}
cd bench
sed -i 's/1000000, //' bench.cpp
g++ %{build_cxxflags} -o bench bench.cpp
./bench
cd -
%endif

%files devel
%doc readme.md
%license license.txt
%{_includedir}/pdqsort.h

%changelog
%autochangelog
