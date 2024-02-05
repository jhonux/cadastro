 $(document).ready(function () {
        clientes_tabela();
    })

    function clientes_tabela() {
        const url = `/clientes_tabela/`;

        fetch(`${url}`)
        .then(response => response.json())
        .then(response => {
            const clientes = response.clientes;

            const tableBody = document.querySelector('#clientesTable tbody');
            tableBody.innerHTML = ''; // Limpa os dados anteriores

            let groupedClientes = {};

            clientes.forEach(cliente => {
                if (!groupedClientes[cliente.id]) {
                    groupedClientes[cliente.id] = {
                        id: cliente.id,
                        nome: cliente.nome,
                        carros: [cliente.veiculo__modelo]
                    };
                } else {
                    groupedClientes[cliente.id].carros.push(cliente.veiculo__modelo);
                }
            });

            Object.values(groupedClientes).forEach(cliente => {
                const carros = cliente.carros.join(', ');

                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${cliente.id}</td>
                    <td>${cliente.nome}</td>
                    <td>${carros}</td>
                    <td><button class="detalhes-btn" data-cliente='${JSON.stringify(cliente)}'>Detalhes</button></td>
                    <td><button class="editar-btn" data-cliente='${JSON.stringify(cliente)}'>Editar</button></td>
                `;
                tableBody.appendChild(row);
            });

            const detalhesButtons = document.querySelectorAll('.detalhes-btn');
            detalhesButtons.forEach(button => {
                button.addEventListener('click', abrirModal);
            });

            const editarButtons = document.querySelectorAll('.editar-btn');
            editarButtons.forEach(button => {
                button.addEventListener('click', redirecionarParaPaginaEditar);
            });
        });
    }

    function redirecionarParaPaginaEditar(event) {
        const cliente = JSON.parse(event.target.getAttribute('data-cliente'));
        const clienteId = cliente.id;
        window.location.href = `/editar_cliente/${clienteId}`;
    }



    function abrirModal(event) {
    const cliente = JSON.parse(event.target.getAttribute('data-cliente'));
    const detalhesCliente = document.querySelector('#detalhesCliente');

    let carrosC = "";
    cliente.carros.forEach(carro => {
        carrosC += `<p>${carro}</p>`;
    })
    detalhesCliente.innerHTML = `
        <p>ID: ${cliente.id}</p>
        <p>Nome: ${cliente.nome}</p>
        <p>Veículo: ${carrosC}</p>
        <!-- Adicione mais detalhes conforme necessário -->
    `;

    const modal = new bootstrap.Modal(document.getElementById('clienteModal'));
    modal.show();
}

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }