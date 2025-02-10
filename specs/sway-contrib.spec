Name:           sway-contrib
Version:        1.10.1
Release:        %autorelease
Summary:        Collection of user-contributed scripts for Sway

License:        MIT
URL:            https://github.com/OctopusET/sway-contrib
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  scdoc

Requires:       sway
Requires:       python3dist(i3ipc)

%description
%{summary}.

%package -n     grimpicker
Summary:        A simple color picker for wlroots
Requires:       grim
Requires:       slurp
Recommends:     /usr/bin/wl-copy
Recommends:     /usr/bin/notify-send

%description -n grimpicker
grimpicker is a color picker that uses slurp and grim.

%package -n     grimshot
Summary:        Helper for screenshots within sway
Requires:       grim
Requires:       jq
Requires:       slurp
Requires:       sway
Requires:       /usr/bin/wl-copy
Recommends:     /usr/bin/notify-send

%description -n grimshot
Grimshot is an easy to use screenshot tool for sway. It relies on grim,
slurp and jq to do the heavy lifting, and mostly provides an easy to use
interface.


%prep
%autosetup
%py3_shebang_fix grimpicker/grimpicker *.py


%build
%make_build -C grimpicker
scdoc <grimshot/grimshot.1.scd >grimshot/grimshot.1


%install
install -D -pv -t %{buildroot}%{_libexecdir}/%{name}  *.py
# grimpicker
%make_install -C grimpicker PREFIX=%{_prefix}
install -D -pv -m0644 grimpicker/completion.zsh \
    %{buildroot}%{zsh_completions_dir}/_grimpicker
# grimshot
install -D -pv -m0644 grimshot/grimshot.1 \
    -t %{buildroot}%{_mandir}/man1
install -D -pv -m0755 grimshot/grimshot \
    -t %{buildroot}%{_bindir}
install -D -pv -m0644 grimshot/grimshot-completion.bash \
    %{buildroot}%{bash_completions_dir}/grimshot


%files
%license LICENSE
%doc README.md
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*.py

%files -n grimpicker
%license LICENSE
%{_bindir}/grimpicker
%{_mandir}/man1/grimpicker.1*
%{bash_completions_dir}/grimpicker
%{fish_completions_dir}/grimpicker.fish
%{zsh_completions_dir}/_grimpicker

%files -n grimshot
%license LICENSE
%{_bindir}/grimshot
%{_mandir}/man1/grimshot.1*
%{bash_completions_dir}/grimshot


%changelog
%autochangelog
