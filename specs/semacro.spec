Name:           semacro
Version:        0.2.1
Release:        %autorelease
Summary:        Explore and expand SELinux policy macros, interfaces, and templates

License:        MIT
URL:            https://github.com/pranlawate/semacro
VCS:            git:https://github.com/pranlawate/semacro.git
Source0:        https://github.com/pranlawate/semacro/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       selinux-policy-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  selinux-policy-devel

%description
semacro parses the SELinux reference-policy macro library and provides
quick lookup, search, and recursive expansion of interfaces, templates,
and defines.  It can substitute arguments, recursively expand nested
calls into a tree of final policy rules, and output flat copy-paste-ready
rules for use in .te policy files.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build (pure Python script) 


%install
install -Dm755 semacro.py       %{buildroot}%{_bindir}/semacro
install -Dm644 semacro.1        %{buildroot}%{_mandir}/man1/semacro.1

install -Dm644 completions/semacro.bash \
    %{buildroot}%{bash_completions_dir}/semacro
install -Dm644 completions/semacro.zsh \
    %{buildroot}%{zsh_completions_dir}/_semacro

%py3_shebang_fix %{buildroot}%{_bindir}/*

%check
%{python3} -m pytest tests/

%files
%license LICENSE
%doc README.md CONTRIBUTING.md ROADMAP.md
%{_bindir}/semacro
%{_mandir}/man1/semacro.1*
%{bash_completions_dir}/semacro
%{zsh_completions_dir}/_semacro

%changelog
%autochangelog
