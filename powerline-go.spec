# https://github.com/justjanne/powerline-go
%global goipath         github.com/justjanne/powerline-go
Version:                1.22.1

%gometa

%global common_description %{expand:
A Powerline like prompt for Bash, ZSH and Fish.

 - Shows some important details about the git/hg branch
 - Changes color if the last command exited with a failure code
 - If you're too deep into a directory tree, shortens the displayed
   path with an ellipsis
 - Shows the current Python virtualenv environment
 - It's easy to customize and extend.}

Name:           powerline-go
Release:        %autorelease
Summary:        A beautiful and useful low-latency prompt for your shell, written in go

License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/powerline-go %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*

%changelog
%autochangelog
