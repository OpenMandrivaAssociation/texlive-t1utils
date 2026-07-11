%global tl_name t1utils
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Simple Type 1 font manipulation programs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/t1utils
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/t1utils.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/t1utils.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(t1utils.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of simple programs for manipulating Adobe Type 1 fonts,
comprising: - t1ascii: convert PFB (binary) to PFA (ascii) fonts; -
t1binary: convert PFA to PFB fonts; - t1disasm: convert PFA or PFB fonts
to human-readable and -editable format; - t1asm: reassemble such
editable formats to a font; - t1unmac: extract font resources from a
Macintosh font file; and - t1mac: generate a Macintosh font from a Type
1 font.

