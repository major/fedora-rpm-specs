Name:           sc-im         
Version:        0.8.4
Release:        %autorelease
Summary:        Spreadsheet Calculator Improvised, ncurses based vim-like spreadsheet calculator 

License:        BSD-4-Clause 
URL:            https://github.com/andmarti1424/sc-im           
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz      

Patch:          0001-fix-for-gcc-incompatability.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  byacc
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  %{_bindir}/pkg-config
BuildRequires:  pkgconfig(libxls)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lua)
Recommends:     gnuplot
Recommends:     xclip

#Currently disabled as tests are inactive
#BuildRequires:   valgrind

%description
Spreadsheet Calculator Improvised, aka sc-im, is an ncurses based, vim-like
spreadsheet calculator. sc-im is based on sc, whose original authors are James
Gosling and Mark Weiser, and mods were later added by Chuck Martin.

%prep
#Adjust name because extracted folder lacks letter v in version
%autosetup -p1 -n sc-im-%{version}

%build
# Modify the Makefile to comply with the FHS 
%make_build -C src/

%install
%make_install prefix=%{_prefix} -C src/

#Currently the tests fail due to additional string "No such device or address" is attached to end result
#Issue is under investigation, the problem seems to be with concating of the outputs in the test scripts
#Specifically with the part '2>&1' of the assert call
#Also test7 is currently reported as unfunctional
#%%check
#pushd tests
#mv test7.sh test7.sh.known-fail
#./run_all_tests.sh
#popd

%files
%license  LICENSE doc/grammar_yacc_tools/y2l.license
%doc CHANGES Readme.md BUGS HELP KNOWN_ISSUES USER_REQUESTS WIKI  doc/grammar_yacc_tools/y2l.readme

%dir %{_datadir}/sc-im
%{_bindir}/sc-im
%{_bindir}/scopen
#manpages
%{_mandir}/man1/sc-im.1*

# Data files in share directory
%{_datadir}/sc-im/plot_bar
%{_datadir}/sc-im/plot_line
%{_datadir}/sc-im/plot_pie
%{_datadir}/sc-im/plot_scatter
%{_datadir}/sc-im/sc-im_help

%changelog
%autochangelog
