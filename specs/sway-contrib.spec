Name:           sway-contrib
Version:        1.12
Release:        %autorelease
Summary:        Collection of user-contributed scripts for Sway

License:        MIT
URL:            https://github.com/OctopusET/sway-contrib
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

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
#Recommends:     wayfreeze

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
#Recommends:     wayfreeze

%description -n grimshot
Grimshot is an easy to use screenshot tool for sway. It relies on grim,
slurp and jq to do the heavy lifting, and mostly provides an easy to use
interface.


%prep
%autosetup
%py3_shebang_fix grimpicker/grimpicker *.py


%build
for man in grimpicker/grimpicker.1 grimshot/grimshot.1; do
    scdoc <"${man}.scd" >"${man}"
done


%install
install -D -pv -t %{buildroot}%{_libexecdir}/%{name}  *.py
# grimpicker, grimshot
install -D -pv -m0755 -t %{buildroot}%{_bindir} \
    grimpicker/grimpicker grimshot/grimshot
install -D -pv -m0644 -t %{buildroot}%{_mandir}/man1 \
    grimpicker/grimpicker.1 grimshot/grimshot.1
# completions
install -D -pv -m0644 grimpicker/completion.bash \
    %{buildroot}%{bash_completions_dir}/grimpicker
install -D -pv -m0644 grimpicker/completion.fish \
    %{buildroot}%{fish_completions_dir}/grimpicker.fish
install -D -pv -m0644 grimpicker/completion.zsh \
    %{buildroot}%{zsh_completions_dir}/_grimpicker
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
